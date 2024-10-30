from django import forms
from .models import Note

class NayaNote(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('name', 'description', 'category')