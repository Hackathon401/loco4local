from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_business/', views.create_business, name='create_business'),
    path('vendor_info/<list_id>', views.vendor_info, name='vendor_info'),
    path('business_info/', views.business_info, name='business_info'),
    path('account_info/', views.account_info, name='account_info'),
]