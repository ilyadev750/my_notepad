from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import View
from .models import Article
from .forms import ArticleForm
from.process import html_to_pdf

# class GeneratePdf(View):
#      def get(self, request, *args, **kwargs):
         
#         # getting the template
#         pdf = html_to_pdf('result.html', kwargs)
         
#          # rendering the template
#         return HttpResponse(pdf, content_type='application/pdf')

def index(request, *args, **kwargs):
    articles = Article.objects.all()
    my_context = {"articles": articles}
    return render(request, 'article/index.html', my_context)

def note(request, *args, **kwargs):
    article = Article.objects.get(id=1)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form = ArticleForm(title=form.title, content=form.content)
            # pdf = html_to_pdf('note.html', {'article': article, 'form': form})
            # return HttpResponse(pdf, content_type='application/pdf')
        
    else:
        form = ArticleForm(instance=article)

    return render(request, 'article/note.html', {'form': form})
