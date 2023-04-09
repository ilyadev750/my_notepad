from django.utils import timezone

def prepare_data_for_form(request):
    try:
        title = request.session['title']
        content = request.session['content']
    except:
        title = ''
        content = ''
    data = {'title': title, 
            'content': content, 
            'create': timezone.now(), 
            'update': timezone.now()}
    return data

def add_info_in_object(obj, form):
    obj.title = form.cleaned_data['title']
    obj.content = form.cleaned_data['content']
    obj.create = form.cleaned_data['create']
    obj.update = form.cleaned_data['update']
    return obj