from django.urls import path
from orderapp import views
urlpatterns = [
    path('index/', views.indexPage),
    path('details/', views.detailPage),
]
