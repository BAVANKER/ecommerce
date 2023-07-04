from django.urls import path
from . import views
app_name = 'shop'
# ADMIN NAME: original, PASSWORD: 1234, ENV NAME: shoppee, DATA BASE NAME: newshop,
# CONTEXT NAME: shop.context_processors.menu_links, PROJECT: ecommerce


urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProDetail, name='prodcatdetail'),
]
