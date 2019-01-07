from django.shortcuts import render
from .models import Category, Product
from django.db import models


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(availabe=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        # TODO: get_object_or_404
        products = products.filter(category=category)
    return render(request, 'shop/products/list.html', {'category': category,
                                                       'categories': categories,
                                                       'products': products})


def products_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    # TODO: get_object_or_404
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

def get_object_or_404(Product, id, slug, available=True):
    