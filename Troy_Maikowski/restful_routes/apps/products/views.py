from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Product

from datetime import datetime
# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/index.html', context)

def show(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'products/show.html', context)

def edit(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'products/edit.html', context)

def update(request, id):
    if request.method == "POST":
        product = Product.objects.get(id=id)
        product.name = request.POST['prod_name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.updated_at = datetime.now()
        product.save()
    return redirect(reverse('products:index'))

def add(request):
    return render(request, 'products/new.html')

def create(request):
    if request.method == "POST":
        name = request.POST['prod_name']
        description = request.POST['description']
        price = request.POST['price']
        Product.objects.create(name=name, description=description, price=price)
    return redirect(reverse('products:index'))

def destroy(request, id):
    Product.objects.filter(id=id).delete()
    return redirect(reverse('products:index'))
