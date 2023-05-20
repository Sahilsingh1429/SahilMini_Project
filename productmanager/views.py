from django.shortcuts import render,redirect
from .models import *
from Admin.models import *

# Create your views here.

def index(request):
    u1 = Product_Sub_Cat.objects.all()
    return render(request,'index2.html',{'sss':u1})


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        username = request.POST['username']
        if username == 'admin':
            request.session['username'] = username
            return redirect('admin_index')
        else:
            request.session['username'] = username
            return redirect('index')
        
def search(request):
    u1 = Product_Sub_Cat.objects.filter(product__name__icontains = request.GET['search'])
    return render(request,'index2.html',{'sec':u1})

def logout(request):
    # del request.session['username'] = username
    return redirect("login")