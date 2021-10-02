from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid")
            return redirect('login')

    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        x1 = request.POST['username']
        y2 = request.POST['firstname']
        z1 = request.POST['lastname']
        z2 = request.POST['email']
        c1 = request.POST['password']
        c2 = request.POST['password1']
        if c1==c2:
           if User.objects.filter(username=x1).exists():
               messages.info(request,"User Name Taken")
               return redirect('register')

           elif User.objects.filter(email=z2).exists():
               messages.info(request, "Email Already Exists")
               return redirect('register')
           else:
                user=User.objects.create_user(username=x1,password=c1,first_name=y2,last_name=z1,email=z2)
                user.save();

                return redirect('login')

        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')