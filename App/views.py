from django.shortcuts import render,redirect ,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from App import models
from App.models import Task,feedback
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        email=request.POST.get('email')
        pwd= request.POST.get('pwd')
        print(fnm,email,pwd)
        my_user=User.objects.create_user(fnm,email,pwd)
        my_user.save()
        return redirect('/login')
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        review = feedback(email=email, desc=desc)
        review.save()
        messages.success(request,"Your message have been sent!")
        
    return render(request, 'contact.html')     
         

def login1(request):
     if request.method == 'POST':
         fnm=request.POST.get('fnm')
         pwd=request.POST.get('pwd')
         userr=authenticate(request, username=fnm, password=pwd)
         if userr is not None:
             login(request, userr)
             return redirect('/todo')
         else:
             return redirect('/login')
         

     return render(request, 'login.html')

def TOdo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.Task(title=title, user=request.user)
        obj.save()
        res = models.Task.objects.filter(user=request.user).order_by('-date')
        return redirect('/todo', {'res':res})
    
    res = models.Task.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'res': res})

def delete_todo(request,srno):
    todo = models.Task.objects.get(srno=srno)
    print(srno)
    todo.delete()
    return redirect('todo')
