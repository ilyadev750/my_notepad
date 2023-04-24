from django.utils import timezone
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  

def prepare_data_for_form(request):
    title = extract_data_from_session(request, 'title')
    content = extract_data_from_session(request, 'content')
    data = {'title': title, 
            'content': content, 
            'create': timezone.now(), 
            'update': timezone.now(),
            'username': 'anonymous'}
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

def add_info_in_object_and_session(obj, form, request):
    obj.title = form.cleaned_data['title']
    obj.content = form.cleaned_data['content']
    obj.create = form.cleaned_data['create']
    obj.update = form.cleaned_data['update']
    obj.username = request.user.username
    request.session['title'] = obj.title
    request.session['content'] = obj.content
    return obj, request

def render_to_pdf(template_src, context={}):
    template = get_template(template_src)
    html  = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), dest=result) 
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('Errors')

