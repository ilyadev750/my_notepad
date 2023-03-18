from django.forms import ModelForm, CharField
from ckeditor.widgets import CKEditorWidget
from .models import Article
from ckeditor.fields import RichTextField

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'