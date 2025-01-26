# urls.py
from django.urls import path
from . import views 


urlpatterns = [
    
    path('', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),


    path('manage_farmers/', views.manage_farmers, name='manage_farmers'),
    path('edit_farmer/<int:pk>/', views.edit_farmer, name='edit_farmer'),
    path('delete_farmer/<int:pk>/', views.delete_farmer, name='delete_farmer'),
]
