from django.db.models import Q
from .models import Note
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from pytils.translit import slugify


def prepare_data_for_form(request):
    title = extract_data_from_session(request, 'title')
    content = extract_data_from_session(request, 'content')
    data = {'title': title,
            'content': content,
            'create': datetime.now(),
            'update': datetime.now(),
            'username': 'anonymous'}
    return data


def extract_data_from_object(obj):
    title = obj.title
    content = obj.content
    update = datetime.now()
    data = {'title': title,
            'content': content,
            'update': update}
    return data


def extract_data_from_session(request, key):
    try:
        value = request.session[key]
    except KeyError:
        value = ''
    return value


def extract_data_from_form(form, key):
    try:
        value = form.cleaned_data[key]
    except KeyError:
        value = ''
    return value


def add_info_in_session(form, request):
    if form.is_valid():
        title = extract_data_from_form(form, 'title')
        content = extract_data_from_form(form, 'content')
        request.session['title'] = title
        request.session['content'] = content
    return request


def add_info_in_new_object(obj, cleaned_data, username):
    obj.title = cleaned_data['title']
    obj.content = cleaned_data['content']
    obj.create = cleaned_data['create']
    obj.update = cleaned_data['update']
    obj.username_id = User.objects.get(username=username)
    obj.slug = slugify(obj.title) + get_random_string(length=8)
    return obj


def add_info_in_current_object(obj, cleaned_data):
    if obj.title != cleaned_data['title']:
        obj.title = cleaned_data['title']
        obj.slug = slugify(obj.title) + get_random_string(length=8)
    obj.content = cleaned_data['content']
    obj.update = cleaned_data['update']
    return obj


def get_queryset_from_db(username, slug):
    q1 = Q(username_id__username=username)
    q2 = Q(slug=slug)
    current_note_object = (
        Note.objects.select_related('username_id')
        .filter(q1 & q2)
        )
    return current_note_object


def reset_session(request):
    request.session['title'] = ''
    request.session['content'] = ''
