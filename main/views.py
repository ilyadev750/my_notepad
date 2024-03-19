from django.shortcuts import redirect
from django.shortcuts import render
from .tasks import send_email_to_user as email_to_user


def index(request):
    context = {"user": request.user}
    return render(request, 'main/index.html', context)


def about(request):
    context = {"user": request.user}
    return render(request, 'main/about.html', context)


def send_mail(request):
    subject = f"{request.GET.get('name')}, {request.GET.get('email')}"
    from_email = None
    message = request.GET.get('message')
    recipient_list = ['petrovich7600@yandex.ru']
    email_to_user.delay(
        subject=subject, message=message, 
        from_email=from_email,
        recipient_list=recipient_list,
        )
    return redirect('home')    

