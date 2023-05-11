from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpRequest
from rest_framework.response import Response
from api.models import SalesRepresentative
from api.serializers import SalesRepresentativeSerializer
# Create your views here.




@api_view(['GET'])
def user_account(request,phone_number):
    serializer_context = {
        'request': request,
    }
    print(request)
    sales_representative = SalesRepresentative.objects.get(phone_number=phone_number)
    data = SalesRepresentativeSerializers(sales_representative, context=serializer_context).data
    print(data)

    return Response(data)
