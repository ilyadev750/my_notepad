from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponseRedirect


def login_user(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']
        except MultiValueDictKeyError as exc:
            return redirect('login')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('http://127.0.0.1:8000/')
        else:
            messages.success(request, ("There was an error, try again ..."))
            return redirect('login')
    return render(request, 'authenticate/login.html', {})

