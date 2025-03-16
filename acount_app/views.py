from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth  import login,authenticate,logout
from .models import Profile


def acount(request):
         print(request.user.is_authenticated) 
         if  request.method=="POST":
                 name=request.POST.get('username')
                 passw=request.POST.get('password')
                 user=authenticate(request,username=name,password=passw)
                 if user is not None:
                         login(request,user)
                         return redirect('/blog')  
         return render(request,"acount_app/login.html")
def sing_out(request):
        
        logout(request)
        return redirect('/blog')
           
                
def registration(request):
         
         if request.method=="POST":
                name=request.POST.get('name')
                last_name=request.POST.get('last_name')
                Email=request.POST.get('Email')
                password1=request.POST.get('password1')
                password2=request.POST.get('password2')
                hashed_password = make_password(password1)
                if password1  != password2:
                                 return render(request,"acount_app/registration.html",context={"password":password1})

                
                user=User.objects.create(username=name,last_name=last_name,email=Email,password=hashed_password) 
                user.save
                login(request,user)
                return redirect('home_app:main')    
                
         return render(request,"acount_app/registration.html")
        
      
 
        
def profile(request):
        profile=Profile.objects.all()
        return render(request,"acount_app/profile.html",context={'profile':profile})
        
   
   