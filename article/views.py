from django.shortcuts import render

from .models import Article

def index(request, *args, **kwargs):
    article = Article.objects.get(id=1)
    my_context = {"title": article.title,
    "content": article.content}
    return render(request, 'article/index.html', my_context)
