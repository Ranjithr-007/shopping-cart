from django.urls import path
from .views import login,register,add_products,dashboard,edit_products
urlpatterns=[
    path('',login,name='login'),
    path('dashboard/',dashboard,name='dashboard'),
    path('register/',register,name='register'),
    path('add-products/',add_products,name='add_products'),
    path('edit-products/<int:id>',edit_products,name='edit_products'),
]