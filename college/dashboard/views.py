from os import name
from django.shortcuts import redirect, render
# from .models import registration 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import HttpResponse


# Create your views here.
def course(request):
    return render(request,"course.html")

def index(request):
    return render(request, "index.html")


def profile(request):
    if request.session.has_key('username'):
        s=User.objects.all()
        user=User.objects.filter(username=request.session['username'])
        return render(request, "profile.html",{'res':s,"udata":request.session['username']})
    else:
        return redirect("/login")

def login(request):
    #if request.method == 'post':
    if request.method =="POST":
        username =request.POST.get("username")
        password =request.POST.get("password")
        #print (username,password)
        user=authenticate(request,username=username,password=password)
        if user:
          request.session['username']=request.POST['username']
          #login(user)
          return redirect('/profile')
        #return httpresponse("login to dashboard")
        else:
            return HttpResponse("userid or password incorrect")
    return render (request,"login.html")

def about(request):
    return render(request,"about.html")

def news(request):
    return render(request,"news.html")

def contact(request):
    return render(request,"contact.html")

def home(request):
    return render(request,"home.html")

#def contact(request):
#if request.method=="post"
 #name= request.post['name']
 #email= request.post['email']
 #phone = request.post['phone']
 #desc= request.post['desc']
 #print=(name,phone,email,desc)
 #ins = contact(name=name,email=email,phone=phone,desc=desc)
 #ins.save()
 #print("the data has been written to the db")
#return rennder(request,'contact.html')  

def singup(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['psw']
        cpassword = request.POST['psw-repeat']
        print(email,password)
        if password!=cpassword:
            print("password is not correct")
        else:
            print(name,password,email,cpassword)
            my_user=User.objects.create_user(username=username,email=email,password=password)
            my_user.save()
            return redirect('/login')
   #ins = singup(name=name,email=email,password=password,desc=cpassword)
       #ins.save()
       #print("redirect login page")
    return render(request, 'singup.html')
