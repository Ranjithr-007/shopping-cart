from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import Products

def dashboard(request):
    products = Products.objects.all()
    return render(request,'dashboard.html',{'products':products})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username,password=password)
        print('user',user)
        if user is not None:
            auth.login(request,user)
            print('2222222')
            return redirect(dashboard)
        else:
            return render(request,'login.html')    
    else:        
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
        messages.success(request,'User created Successfully')
        return redirect(login)
    else:    
        return render(request,'register.html')

def add_products(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        product_image = request.FILES.get('product_image')
        Products.objects.create(product_name=product_name,quantity=quantity,price=price,Image=product_image,status=True)
        messages.success(request,'Product Added Successfully')
        return redirect(dashboard)
    else:    
        return render(request,'add_products.html',{'title':'Add Product'})

def edit_products(request,id):
    product = Products.objects.get(id=id)
    if request.method == 'POST':
        product.product_name = request.POST.get('product_name')
        product.quantity = request.POST.get('quantity')
        product.price = request.POST.get('price')
        try:
           image = request.FILES.get('product_image')
        except:
            pass
        if image is None:
            image = product.Image
        product.Image = image        
        product.save()
        messages.info(request,'Product Updated')
        return redirect(dashboard)
    else:    
        return render(request,'add_products.html',{'product':product,'title':'Edit Product'})
        