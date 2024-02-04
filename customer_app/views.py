# Create your views here.
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from customer_app.models import Customer


@api_view(['GET'])
def hello_world(request):
    data = {'message': 'Hello, world!'}
    return Response(data)


@api_view(['GET'])
def get_customers(request):
    all_customers = Customer.objects.all()
    data = []
    for customer in all_customers:
        data.append(
            dict(
                id=customer.id,
                fist_name=customer.first_name,
                last_name=customer.last_name,
                email=customer.email,
                phone_number=customer.phone_number,
            )
        )
    json_data = json.dumps(data)
    return Response(json_data)


@api_view(['POST'])
def add_customer(request):
    customer_data = request.data  # a dict with the request body
    new_customer = Customer.objects.create(
        first_name=customer_data['first_name'],
        last_name=customer_data['last_name'],
        email=customer_data['email'],
        phone_number=customer_data['phone_number'],
    )
    json_data = json.dumps({
        'id': new_customer.id,
        'first_name': new_customer.first_name,
        'last_name': new_customer.last_name,
        'email': new_customer.email,
        'phone_number': new_customer.phone_number
    })
    return Response(json_data)
