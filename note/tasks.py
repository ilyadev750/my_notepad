from distutils.command import clean
from django.shortcuts import redirect
from django.core.cache import cache
from .models import Note
from .functions import add_info_in_new_object
from celery import shared_task


@shared_task
def create_new_note(clean_data, username):
    empty_obj = Note()
    # filled_obj, request = add_info_in_new_object(
    #     empty_obj, form, request
    #     )
    filled_obj = add_info_in_new_object(
        empty_obj, clean_data, username
        )
    cache.delete(username)
    filled_obj.save()
    