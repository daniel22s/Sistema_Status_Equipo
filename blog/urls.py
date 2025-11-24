from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('products/',views.Product_Type,name='product'),
    path('status/',views.status_view,name='status'),
]