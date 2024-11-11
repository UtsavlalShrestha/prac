from django import forms
from .models import Note, NoteCategory, User



class NoteCategryForm(forms.ModelForm):
    class Meta:
        model = NoteCategory
        fields = '__all__'
        widgets ={
            'name': forms.TextInput(attrs={'class':"form-control"})
        }
        


class NayaNote(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('name', 'description', 'category')
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets ={
            'username': forms.TextInput(attrs={'class':"form-control"}),
            'email': forms.TextInput(attrs={'class':"form-control"}),
            'password': forms.PasswordInput(attrs={'class':"form-control"}),
        }
        