from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="cart"),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_quantity/<int:product_id>/', views.update_quantity, name='update_quantity'),
]