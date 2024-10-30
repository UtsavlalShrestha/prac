from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
from .forms import NayaNote
# Create your views here.

def home(request):
    data = Note.objects.all()
    context = {'data': data}
    return render(request, 'index.html', context)

def create(request):
    form = NayaNote()
    if request.method == 'POST':
        form = NayaNote(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Note created')

    context={'form': form}
    return render(request, 'base/create.html', context)
