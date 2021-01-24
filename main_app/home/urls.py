from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # http://localhost:8000/home/create_business/
    path('create_business/', views.create_business, name='create-business'),
    path('vendor_info/', views.vendor_info, name='vendor_info')
]