from django.urls import path
from userapp import views
urlpatterns = [
    path('index/', views.index),
    path('login/',views.login),
    path('logout/',views.logout)
    ]
