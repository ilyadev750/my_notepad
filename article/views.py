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
        form = ArticleForm(request.POST or None, instance=article)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            form = Article.objects.create(title=title, content=content)
            form.save()
            # pdf = html_to_pdf('note.html', {'article': article, 'form': form})
            # return HttpResponse(pdf, content_type='application/pdf')
        
    else:
        form = ArticleForm(instance=article)
    context = {'form': form}

    return render(request, 'article/note.html', context)
