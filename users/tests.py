import uuid
import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.fixture
def test_password():
   return 'strong-test-pass'
    
@pytest.fixture
def create_user(db, django_user_model, test_password):
   def make_user(**kwargs):
       kwargs['password'] = test_password
       if 'username' not in kwargs:
           kwargs['username'] = str(uuid.uuid4())
       return django_user_model.objects.create_user(**kwargs)
   return make_user

@pytest.mark.django_db
def test_auth_view(client, create_user, test_password):
   user = create_user(username='someone')
   url = reverse("login")
   client.login(
       username=user.username, password=test_password
   )
   response = client.get(url)
   assert 'someone' in response.content.decode()
   assert response.status_code == 200
   
@pytest.mark.django_db
def test_create_user(create_user):
    user = create_user(username='someone')
    assert User.objects.count() == 1

