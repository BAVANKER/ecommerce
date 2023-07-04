from django.urls import path
from . import views
app_name = 'cart'


urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('trash/<int:product_id>/', views.cart_trash, name='cart_trash'),
    path('', views.cart_detail, name='cart_detail'),
]
