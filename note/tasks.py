from .forms import UserCreateNoteForm
from django.shortcuts import redirect
from .models import Note
from .functions import add_info_in_new_object
from celery import shared_task


@shared_task
def create_new_note(request):
    form = UserCreateNoteForm(request.POST)
    empty_obj = Note()
    filled_obj, request = add_info_in_new_object(
        empty_obj, form, request
        )
    if "save" in request.POST:
        filled_obj.save()
        return redirect("get_user_notes", request.user.username)