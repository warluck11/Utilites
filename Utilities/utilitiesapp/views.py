from django.shortcuts import render, HttpResponse, redirect
from utilitiesapp.models import services
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import os

# Create your views here.
def home(request):
    return render(request, 'home.html')

def create_service(request):
    
    if request.method == "GET":
        
        return render(request, "serviceform.html")
    
    else:
        
        name = request.POST['name']
        address = request.POST['address']
        email = request.POST['email']
        mobile = request.POST['mobile']
        service = request.POST['service']
        
        
        m = services.objects.create(user = request.user ,name = name, address = address, email = email, 
                                    mobile = mobile, service = service)
        
        m.save()
        
        return redirect('/')
    
def show_services(request):
    
    if request.user.is_staff:
        
        m = services.objects.all()
        
        context = {}
        
        context['data'] = m
        
        return render(request, 'showservice.html', context)
    
    else:
        m = services.objects.filter(user = request.user)
        
        context = {}
        
        context['data'] = m
        
        return render(request, 'showservice.html', context)

def register(request):
    
    if request.method == "GET":
    
        return render(request, 'register.html')
    
    else:
        
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        upassword = request.POST['upassword']
        cpassword = request.POST['cpassword']
        
        if fname == '' or upassword == '' or cpassword == '':
            
            context = {}
            context['msg'] = 'Fields can not be empty'
            
            return render(request, 'register.html', context)
        
        elif upassword != cpassword:
            
            context = {}
            context['msg'] = 'Password and Confirm Password should be same'
            
            return render(request, 'register.html', context)
        
        else:
            
            u = User.objects.create(username = email, first_name = fname, last_name = lname, 
                                    email = email)
            
            u.set_password(upassword)
            
            u.save()
            
            context = {}
            context['msg'] = 'User Register Successfully'
            
            return render(request, 'register.html', context)
        
def user_login(request):
    
    if request.method == "GET":
    
        return render(request, 'login.html')
    
    else:
        
        name = request.POST['email']   
        password = request.POST['password']
        
        u = authenticate(username = name, password = password)
        
        if u is not None:
            
            login(request, u)
            return redirect('/')
        
        else:
            
            context = {}
            context['msg'] = 'Username Password Wrong'
            
            return render(request, 'login.html', context)
        
        
def user_logout(request):
    
    logout(request)
    
    return redirect('/')

def edit_service(request, rid):
    
    
    if request.method == "GET":
        
        m = services.objects.filter(id = rid)
        
        context = {}
        
        context['data'] = m
    
        return render(request, 'editservice.html', context)
    
    else:    
        
        status = request.POST['status']
        
        print(status)
        
        m = services.objects.filter(id = rid)
        
        m.update(status = status)
        
        
        
        return redirect('/showservice')
    
   