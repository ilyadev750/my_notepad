from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from pytils.translit import slugify
from xhtml2pdf import pisa


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
    except:
        value = ''
    return value


def extract_data_from_form(form, key):
    try:
        value = form.cleaned_data[key]
    except:
        value = ''
    return value


def add_info_in_session(form, request):
    if form.is_valid():
        title = extract_data_from_form(form, 'title')
        content = extract_data_from_form(form, 'content')
        request.session['title'] = title
        request.session['content'] = content
    return request


def add_info_in_new_object_and_session(obj, form, request):
    obj.title = form.cleaned_data['title']
    obj.content = form.cleaned_data['content']
    obj.create = form.cleaned_data['create']
    obj.update = form.cleaned_data['update']
    obj.username_id = User.objects.get(username=request.user.username)
    obj.slug = slugify(obj.title) + get_random_string(length=8)
    request.session['title'] = obj.title
    request.session['content'] = obj.content
    return obj, request


def add_info_in_current_object_and_session(obj, form, request):
    if obj.title == form.cleaned_data['title']:
        obj.title = form.cleaned_data['title']
    else:
        obj.title = form.cleaned_data['title']
        obj.slug = slugify(obj.title) + get_random_string(length=8)
    obj.content = form.cleaned_data['content']
    obj.update = form.cleaned_data['update']
    request.session['title'] = obj.title
    request.session['content'] = obj.content
    return obj, request


def render_to_pdf(template_src, context={}):
    template = get_template(template_src)
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),
                                 dest=result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('Errors')


def make_pdf(request):
    context = {
        'title': request.session['title'],
        'content': request.session['content']
        }
    pdf = render_to_pdf('user_note.html', context)
    return pdf
