from distutils.command import clean
from django.shortcuts import redirect
from django.core.cache import cache
from .models import Note
from .functions import add_info_in_new_object, add_info_in_current_object
from celery import shared_task


@shared_task
def create_new_note(cleaned_data, username):
    empty_obj = Note()
    filled_obj = add_info_in_new_object(
        empty_obj, cleaned_data, username
        )
    cache.delete(username)
    filled_obj.save()


@shared_task
def update_current_note(cleaned_data, slug):
    old_obj = cache.get(slug)
    new_obj = add_info_in_current_object(old_obj, cleaned_data)
    cache.delete(slug)
    new_obj.save()
    