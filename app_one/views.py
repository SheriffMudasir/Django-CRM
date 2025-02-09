from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in")
            return redirect('home')
        elif user is None:
            messages.warning(request, "Please click on the register button to register if you haven't")  
        else:
            messages.warning(request, "There was an error login you in")
    return render(request, 'home.html', {'records': records})
    
    

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.warning(request, "You must log in to view this page!")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        record_delete = Record.objects.get(id=pk)
        record_delete.delete()
        messages.success(request, "Record has been successfully deleted")
        return redirect('home')
    else:
        messages.warning(request, "You must log in to view this page!")
        return redirect('home')
    
def add_record(request):
    if request.user.is_authenticated:
        form = AddRecordForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                saved_form = form.save(commit=False)
                saved_form.user = request.user
                saved_form.save()
                messages.success(request, "Record added successfully")
                return redirect('home')
        return render(request, "add_record.html", {'form':form})
    else:
        messages.warning(request, "You must log in to add records")
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        record_update = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=record_update)
        if form.is_valid():
            form.save()
            messages.success(request, "Form has been saved successfully")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.warning(request, "You must be loggin to to update record")
        return redirect('home')
        
        

        