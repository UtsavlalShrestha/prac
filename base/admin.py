from django.contrib import admin
from .models import Note, NoteCategory
# Register your models here.
admin.site.register(NoteCategory)
admin.site.register(Note)