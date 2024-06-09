from django.urls import path
from.views import *

urlpatterns = [
    path("",HomeView.as_view(), name = 'home'),
    path("category/<slug>", CatoegoryView.as_view(),name = 'category'),
    path("brand/<slug>", BrandView.as_view(), name='brand'),
    path("detail/<slug>", DetailView.as_view(), name='detail'),
    path("search/", SearchView.as_view(), name='search'),
    path("signup", signup, name = 'signup'),
    path("cart", CartView.as_view(), name='cart'),
    path("add_to_cart/<slug>", cart, name = 'add_to_cart'),
    path("reduce_quantity/<slug>", reduce_quantity, name='reduce_quantity'),
    path("delete_cart/<slug>", delete_cart, name='delete_cart'),
    path("submit_review/<slug>", submit_review, name='submit_review'),

]
