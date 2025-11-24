from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Equipo_Status
# Create your views here.

def Product_Type(request):
    products = Product.objects.all()
    return render(request,'blog/product.html',{'product':products})

def status_view(request):
    status = Equipo_Status.objects.all().order_by('locate')
    context = {'equipo_list':status}
    return render(request,'blog/status.html',context)