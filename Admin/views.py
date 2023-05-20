from django.shortcuts import render,HttpResponse,redirect
from .models import *
# Create your views here.


def admin_index(request):
    if request.method == 'GET':
        return render(request,'admin_index.html')
    else:
        Product.objects.create(
            name = request.POST['Product_name']
        )
        u1 = Product.objects.get(name=request.POST['Product_name'])
        
        Product_Sub_Cat.objects.create(
            product_price = request.POST['Product_price'],
            product_pic = request.FILES['Product_picture'],
            product_model = request.POST['Product_model'],
            product = u1
        
        )
        
        return render(request,'admin_index.html',{"msg":"Product Information Added Sucessfully!!"})


def view_product(request):
    u2 = Product_Sub_Cat.objects.all()
    
    return render(request,'view_product.html',{"userdata":u2})


def update_product(request):
    return render(request,'update_product.html')


def delete(request,cid):
    c_obj = Product.objects.get(id = cid)
    c_obj.delete()
    return redirect('view_product')