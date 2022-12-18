from django.urls import path
from .views import home,user_login,user_signup,logout,add_cart,cart
urlpatterns=[
    path('',home,name='home'),
    path('login/',user_login, name='login'),
    path('signup/',user_signup, name='signup'),
    path('logout/',logout, name='logout'),
    path('add_cart<int:id>/',add_cart,name='add_cart'),
    path('cart/',cart,name='cart')
]