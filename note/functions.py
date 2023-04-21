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
            'update': timezone.now(),
            'username': 'anonymous'}
    return data

def add_info_in_object_and_session(obj, form, request):
    obj.title = form.cleaned_data['title']
    obj.content = form.cleaned_data['content']
    obj.create = form.cleaned_data['create']
    obj.update = form.cleaned_data['update']
    request.session['title'] = obj.title
    request.session['content'] = obj.content
    return obj, request

# def user_action_selector(request, )