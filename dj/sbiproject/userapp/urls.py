from django.urls import path
from userapp import views
urlpatterns = [
    path('index/', views.indexPage),
    path('details/', views.detailPage),
    path('contactus/', views.contactPage),
]
