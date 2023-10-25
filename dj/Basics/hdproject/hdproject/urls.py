from django.contrib import admin
from django.urls import path
from crmapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/',views.display_Employees)
]
