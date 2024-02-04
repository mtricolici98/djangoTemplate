from django.urls import path

from customer_app.views import hello_world, get_customers, add_customer

urlpatterns = [
    path('hello/', hello_world),
    path('customer/all/', get_customers),
    path('customer/add/', add_customer),
]