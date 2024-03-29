from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm as ResetForm
from celery import shared_task


@shared_task
def send_link(subject_template_name, email_template_name, context,
              from_email, to_email, html_email_template_name):
    context['user'] = User.objects.get(pk=context['user'])

    ResetForm.send_mail(
        None,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name
    )
