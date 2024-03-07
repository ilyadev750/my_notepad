from django.shortcuts import render


def index(request):
    context = {"user": request.user}
    return render(request, 'main/index.html', context)


def about(request):
    context = {"user": request.user}
    return render(request, 'main/about.html', context)
