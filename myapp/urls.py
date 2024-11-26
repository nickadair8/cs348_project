from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sets/", views.sets, name="sets"),
    path('sets/add/', views.set_create, name='set_create'),
    path('sets/edit/<int:set_id>/', views.set_update, name='set_update'),
    path('sets/delete/<int:set_id>/', views.set_delete, name='set_delete'),
    
    path("customers/", views.customers, name="customers"),
    path('customers/add/', views.customer_create, name='customer_create'),
    path('customers/edit/<int:customer_id>/', views.customer_update, name='customer_update'),
    path('customers/delete/<int:customer_id>/', views.customer_delete, name='customer_delete'),
   
    path('review_detail/<int:review_id>/', views.review_detail, name='review_detail'),
]