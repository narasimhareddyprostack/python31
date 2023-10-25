
from django.contrib import admin
from django.urls import path
from userapp import views
from orderapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/index/', views.indexPage),
    path('user/details/', views.detailPage),
    path('order/index/', views.indexPage),
    path('order/details/', views.detailPage),

]
