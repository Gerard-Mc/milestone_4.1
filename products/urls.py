from django.urls import path
from . import views  # from this directory, import views.

''' Path will = products '''
# When the main urls.py is run and told to "includes" products.urls
# it will open this url
# When this url is opened, the program is directed to the
# portfolio view in the "" which is just the products path
urlpatterns = [
    path('', views.portfolio, name='portfolio')
]
