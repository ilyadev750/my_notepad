from django.utils import timezone
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  

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

def render_to_pdf(template_src, content={}):
    template = get_template(template_src)
    html  = template.render(content)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), dest=result) 
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('Errors')

