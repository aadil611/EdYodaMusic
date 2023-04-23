from django.shortcuts import render
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    errors = None
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print('yes valid')
            form.save()
        else:
            print('Errors are ::::::::;>>>>>>>>',form.errors)
            errors = list(form.errors.values())
            form.errors.clear()
            
    return render(request,'users/register.html',{'errors':errors})



def login(request):
    return render(request,'users/login.html')