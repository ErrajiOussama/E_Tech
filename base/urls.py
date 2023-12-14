
from django.urls import path,include
from . import views
urlpatterns = [
    #home
    path('',views.IndexView.as_view(),name="home"),
    path('products/<produits>',views.ProductsView.as_view(),name="products"),
    path('categorie/<str:categorie>',views.CategorieView.as_view(),name="categorie"),
    path('Gammes/<Gammes>',views.GammeView.as_view(),name="Gamme"),
    path('cart',views.Cartview.as_view(),name='Cart'),
    path('add-to-cart',views.AddtocartView.as_view(),name='add-to-cart'),
    path('delete-from-cart',views.delete_item_cartView.as_view(),name='delete-from-cart'),
    path('update-cart',views.update_item_cartView.as_view(),name='update-cart')
]
