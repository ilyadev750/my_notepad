from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from .forms import CustomUserCreationForm


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


# def password_reset_request(request):
#     if request.method == "POST":
#         password_reset_form = PasswordResetForm(request.POST)
#         if password_reset_form.is_valid():
#             data = password_reset_form.cleaned_data["email"]
#             associated_users = User.objects.filter(Q(email=data))
#             if associated_users.exists():
#                 for user in associated_users:
#                     subject = "Password Reset Requested"
#                     email_template_name = "main/password/password_reset_email.txt"
#                     c = {
#                         "email": user.email,
#                         "domain": "127.0.0.1:8000",
#                         "site_name": "Website",
#                         "uid": urlsafe_base64_encode(force_bytes(user.pk)),
#                         "user": user,
#                         "token": default_token_generator.make_token(user),
#                         "protocol": "https",
#                     }
#                     email = render_to_string(email_template_name, c)
#                     try:
#                         send_mail(
#                             subject,
#                             email,
#                             "admin@example.com",
#                             [user.email],
#                             fail_silently=False,
#                         )
#                     except BadHeaderError:
#                         return HttpResponse("Invalid header found.")
#                     return redirect("/password_reset/done/")
#     password_reset_form = PasswordResetForm()
#     return render(
#         request=request,
#         template_name="main/password/password_reset.html",
#         context={"password_reset_form": password_reset_form},
#     )
