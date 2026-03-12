from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),

    path('', views.home),

    path('register/', views.register),

    path("product/<int:id>/",views.product_detail),

    path("add/<int:id>/",views.add_to_cart),

    path('add_to_cart/<int:id>/', views.add_to_cart, name="add_to_cart"),

    path("cart/",views.view_cart)

]