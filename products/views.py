from django.shortcuts import render
from .models import Product, Category

# After the main url is requested, it's directed to the urls in products
# path('portfolio/', include('products.urls'))
# it is told to use the portfolio view in views.portfolio


def portfolio(request):
    """ View displays all products and sorts by categories """
    #  All products loaded
    products = Product.objects.all()
    categories = None
    categories_string = ""

    if request.GET:
        categories = None
        if 'category' in request.GET:
            #  The split() splits the string into a list
            categories = request.GET['category'].split(",")
            #  Products is now reduced to products of thhat category
            products = products.filter(category__name__in=categories)
            if len(categories) > 1:
                for i in range(len(categories)):
                    categories_string += "" + categories[i] + ","
                categories_string = categories_string[:-1]
            else:
                for i in categories:
                    categories_string += i

            if 'sort' in request.GET:
                    sort = request.GET['sort']
                    sortkey = sort

                    if 'direction' in request.GET:
                        direction = request.GET['direction']
                        if direction == 'desc':
                            sortkey = f'-{sortkey}'
                            products = products.order_by(sortkey)

    context = {
        'products': products,
        'category' : categories_string,
    }

    return render(request, 'products/portfolio.html', context)
