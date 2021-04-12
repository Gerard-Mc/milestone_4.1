from django.shortcuts import render
from .models import Product, Category

# After the main url is requested, then directed(includes) to the urls in products
# it is told to use the portfolio view. views.portfolio
def portfolio(request):
    """ View displays all products and sorts by categories """

    products = Product.objects.all()
    categories = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']

        if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
        products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            #  The split() splits the string into a list
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'products': products,
    }

    return render(request, 'products/portfolio.html', context)
