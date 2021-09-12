from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def categories(request):  # made a rule in setting under templates to make it available for all templates
    return {
        'categories': Category.objects.all()
    }

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'Storage/products/category.html', {'products': products, 'category': category})

def all_products(request):
    products = Product.objects.all()
    return render(request, 'Storage/home.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'Storage/products/detail.html', {'product': product})
