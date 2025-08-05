from django import forms
from app_Admin.models import Teacher,Student, Announcement
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'tragetClass']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        self.fields['tragetClass'].widget.attrs['multiple'] = True