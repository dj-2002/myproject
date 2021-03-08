from django.shortcuts import render
from myapp.models import products
# Create your views here.

def index(request):
    return render(request,'index.html')

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def shop(request):
    return render(request,'shop.html')

def single(request):
    data= products.objects.all()
    context={
        "data":data
    }
    return render(request,'single-product.html',context)                