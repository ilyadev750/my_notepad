from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView 
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError


from .forms import CustomUserCreationForm, UserForgotPasswordForm, UserSetNewPasswordForm


def register_user(request, *args, **kwargs):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration successful"))
            return redirect("get_user_notes", request.user.username)
        elif "home" in request.POST:
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/registration.html", {"form": form})


def login_user(request, *args, **kwargs):
    if request.method == "POST":
        try:
            username = request.POST["username"]
            password = request.POST["password"]
        except MultiValueDictKeyError as exc:
            return redirect("login")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("get_user_notes", request.user.username)
        else:
            messages.success(request, ("There was an error, try again ..."))
            return redirect("login")
    return render(request, "users/login.html", {})


def logout_user(request, *args, **kwargs):
    logout(request)
    return redirect("home")



class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    form_class = UserForgotPasswordForm
    template_name = 'users/password_reset.html'
    success_url = reverse_lazy('home')
    success_message = 'Mail with instructions sent to your email!'
    subject_template_name = 'users/password_subject_reset_mail.txt'
    email_template_name = 'users/password_reset_mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Request to the new password'
        return context


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    form_class = UserSetNewPasswordForm
    template_name = 'users/password_set_new.html'
    success_url = reverse_lazy('home')
    success_message = 'Your password was sucessfully changed. Return to the website.'
               
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Set the new password:'
        return context