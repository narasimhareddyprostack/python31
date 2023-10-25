
from django.contrib import admin
from django.urls import path
from empapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', views.display_User),
    path('employee/', views.display_Employee),
]
