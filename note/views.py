from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.core.cache import cache
from django.utils import timezone
from django.template.loader import render_to_string
from .models import Note
from .forms import NoteForm, UserForm

# Create your views here.
def start(request,*args, **kwargs):
    context = {}
    return render(request, 'note/editor.html', context)

def note(request, *args, **kwargs):
    try:
        data = {'title': request.session['title'], 
                'content': request.session['content'], 
                'create': timezone.now(), 
                'update': timezone.now()}   
        # data = {'title': cache.get('title'), 
        #         'content': cache.get('content'), 
        #         'create': timezone.now(), 
        #         'update': timezone.now()}
    except:
        data = {'title': '', 
                'content': '', 
                'create': timezone.now(), 
                'update': timezone.now()}
    form = NoteForm(data)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            obj = Note()
            obj.title = form.cleaned_data['title']
            obj.content = form.cleaned_data['content']
            obj.create = form.cleaned_data['create']
            obj.update = form.cleaned_data['update']
            # cache.set('title', obj.title)
            # cache.set('content', obj.content)
            request.session['title'] = obj.title
            request.session['content'] = obj.content
            if request.user.is_authenticated:
                obj.save()
            else:
                # return render(request, 'authenticate/login.html', {})
                rendered = render_to_string('authenticate/login.html', {})
                return HttpResponse(rendered)
                # return redirect('login_user', obj.title, obj.content)
                # return HttpResponseRedirect('users/login_user/')
                # context = {'form': form}
                # render(request, 'note/editor.html', context)
                form = NoteForm(request.POST)
    context = {'form': form}
    return render(request, 'note/editor.html', context)



def http_response_view(request):
    return HttpResponse('<h1>This is a H1 heading!</h1>') 

# реализовать создание юзеров, дать им разрешения, foreigh key изучить