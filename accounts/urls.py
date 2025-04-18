from django.urls import path 
from .views import home,user_register,user_login,user_dashboard,user_logout

urlpatterns = [
    path('',home,name='home'),
    path('signup/',user_register,name='signup'),
    path('login/',user_login,name='login'),
    path('profile/',user_dashboard,name='profile'),
    path('logout/',user_logout,name='logout'),
]
