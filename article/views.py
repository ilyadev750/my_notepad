from django.shortcuts import render

from .models import Article
from .forms import ArticleForm

def index(request, *args, **kwargs):
    articles = Article.objects.all()
    my_context = {"articles": articles}
    return render(request, 'article/index.html', my_context)

def note(request, *args, **kwargs):
    article = Article.objects.get(id=1)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=Article)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArticleForm(instance=article)

    return render(request, 'article/note.html', {'article': article, 'form': form})
