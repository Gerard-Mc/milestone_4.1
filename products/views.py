from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category


def products(request):
    """ View displays all products and sorts by categories """

    products = Product.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)


    context = {
        'products': products,
        'current_categories': categories,
    }

    return render(request, 'products/portfolio.html', context)
