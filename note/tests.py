import pytest
import uuid
from .models import Note
from users.tests import create_user
from django.contrib.auth.models import User
from users.tests import test_password


@pytest.mark.django_db
def test_create_note(create_user):
    user = User()
    user.username = 'someone'
    user.save()
    note = Note()
    note.title = 'hello'
    note.content = 'hello'
    note.username_id = user
    note.save()
    assert Note.objects.count() == 1
