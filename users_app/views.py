from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CustomerRegisterForm

def register(request):
    if request.method=="POST":
        register_form = CustomerRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("New User Account Created. Login to get Started"))
            return redirect('todolist')
    else:
        register_form= CustomerRegisterForm()
   
    return render(request, 'register.html',{'register_form':register_form})
    
  