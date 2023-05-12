from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm


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
            return redirect("new_user_note", request.user.id, "current")
    else:
        form = CustomUserCreationForm()
    return render(request, "authenticate/register_user.html", {"form": form})


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
            return redirect("new_user_note", request.user.id, "current")
        else:
            messages.success(request, ("There was an error, try again ..."))
            return redirect("login")
    return render(request, "authenticate/login.html", {})


def logout_user(request, *args, **kwargs):
    logout(request)
    return redirect("/base/")


def reset_password(request, *args, **kwargs):
    pass


def set_password(request, *args, **kwargs):
    pass
