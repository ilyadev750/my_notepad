from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import (UserCreationForm,
                                       SetPasswordForm)
from django.contrib.auth.forms import PasswordResetForm as PasswordResetFormCore
from django.core.exceptions import ValidationError
from .tasks import send_mail


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="Username", min_length=5, max_length=50)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password",
                                widget=forms.PasswordInput)

    def username_clean(self):
        username = self.cleaned_data["username"].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username

    def email_clean(self):
        email = self.cleaned_data["email"].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError("Email Already Exist")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data["username"],
            self.cleaned_data["email"],
            self.cleaned_data["password1"],
        )
        return user


class UserForgotPasswordForm(PasswordResetFormCore):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    def send_mail(self, subject_template_name, email_template_name, context, 
                  from_email, to_email, html_email_template_name=None):
        context['user'] = context['user'].id

        send_mail(subject_template_name=subject_template_name, 
                    email_template_name=email_template_name,
                    context=context, from_email=from_email, to_email=to_email,
                    html_email_template_name=html_email_template_name)
    

class UserSetNewPasswordForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })
