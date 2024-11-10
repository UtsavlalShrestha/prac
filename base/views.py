from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note, NoteCategory
from .forms import NayaNote, NoteCategryForm
# Create your views here.

def home(request):
    context = {}
    return render(request, 'home.html', context)

def list(request):
    data = Note.objects.all()
    note_category = NoteCategory.objects.all()
    context = {'data': data, 'note_category':note_category}
    return render(request, 'index.html', context)

def choose_category(request):
    form = NoteCategryForm()
    if request.method == 'POST':
        form = NoteCategryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    context={'form': form}
    return render(request, 'base/choose_category.html', context)



def create_note(request):
    form = NayaNote()
    if request.method == 'POST':
        form = NayaNote(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')

    context={'form': form}
    return render(request, 'base/create_note.html', context)


def edit_category(request, pk):
    category_obj = NoteCategory.objects.get(id=pk)
    form = NoteCategryForm(instance=category_obj)
    if request.method == 'POST':
        form = NoteCategryForm(request.POST, instance=category_obj)
        if form.is_valid():                
                form.save()
                return redirect('list')
        else:
            return render(request,'base/edit_category.html', context={'form':form})

                
    context = {'form': form}
    return render(request, 'base/edit_category.html', context)

def edit_note(request, pk):
    note_obj = Note.objects.get(id=pk)
    form = NayaNote(instance=note_obj)
    if request.method == 'POST':
        form = NayaNote(request.POST, instance=note_obj)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            return render(request,'base/edit_note.html', context={'form':form})
        
    context = {'form': form}
    return render(request, 'base/edit_note.html', context)

