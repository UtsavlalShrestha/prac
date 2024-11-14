from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Note, NoteCategory
from .forms import NayaNote, NoteCategryForm, UserForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    form  = UserForm()
    if request.method == 'POST':
        password = request.POST.get('password')
        hash_password = make_password(password)
        data = request.POST.copy()
        data['password'] = hash_password
        form = UserForm(data)
        if form.is_valid():
            form.save()
            # return redirect('login')
        else:
            return HttpResponse("Invalid form")
    context = {'form': form}
    return render(request, 'base/register.html', context)

def login_user(request):
    form=UserForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'base/login.html', context={'form':form, 'error': "Invalid username or password"})
    context = {'form': form}
    return render(request,'base/login.html', context)

def logout_user(request):
    logout(request) 
    return redirect('home')




def home(request):
    context = {}
    return render(request, 'home.html', context)


@login_required
def list(request):
    data = Note.objects.filter(user=request.user).order_by('id')
    note_category = NoteCategory.objects.filter(user=request.user).order_by('id')
    context = {'data': data, 'note_category':note_category}
    return render(request, 'index.html', context)


@login_required
def choose_category(request):
    form = NoteCategryForm()
    if request.method == 'POST':
        form = NoteCategryForm(request.POST)
        if form.is_valid():
            note_category = form.save(commit=False)
            note_category.user = request.user
            note_category.save()
            return redirect('list')
    context={'form': form}
    return render(request, 'base/choose_category.html', context)


@login_required
def create_note(request):
    form = NayaNote()
    if request.method == 'POST':
        form = NayaNote(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('list')
        else:
            form = NayaNote()
    context={'form': form}
    return render(request, 'base/create_note.html', context)

@login_required
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

@login_required
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


@login_required
def delete_category(request, pk):
    category_obj = NoteCategory.objects.get(id=pk)
    if request.method == 'POST':
        category_obj.delete()
        return redirect('list')
    return redirect('/')
    

@login_required
def delete_note(request, pk):
    note_obj = Note.objects.get(id=pk)
    if request.method == 'POST':
        note_obj.delete()
        return redirect('list')
    return redirect('/')

