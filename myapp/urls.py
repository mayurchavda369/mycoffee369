from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('register/', views.register,name='register'),
    path('otp/', views.otp,name='otp'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('service/',views.service,name='service'),
    path('booktable/',views.booktable,name='booktable'),
    path('cust/',views.cust,name='cust'),
    path('about/',views.about,name='about'),
    


]
