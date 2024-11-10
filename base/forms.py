from django import forms
from .models import Note, NoteCategory



class NoteCategryForm(forms.ModelForm):
    class Meta:
        model = NoteCategory
        fields = '__all__'
        widgets ={
            'name': forms.Textarea(attrs={'class':"form-control"})
        }
        


class NayaNote(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('name', 'description', 'category')
        