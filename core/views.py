from django.shortcuts import render

from .models import Category, Product


def all_products(request):
    products = Product.products.all()
    return render(request, 'store/home.html', {'products': products})
