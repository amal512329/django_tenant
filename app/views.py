from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Client,Domain
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
# Create your views here.

def index(request):

    return HttpResponse('Hello Public')



class CreateClientView(APIView):
    authentication_classes = []
    permission_classes=[AllowAny]
    def post(self, request):
        client_name = request.data.get('client_name')
        client_display_name = request.data.get('client_display_name')  # If client has a display name

        # Create a new tenant
        new_client = Client(schema_name=client_name, name=client_display_name if client_display_name else client_name)
        new_client.save()

        # Set up the subdomain for the new client
        new_domain = Domain(domain=f"{client_name}.localhost", tenant=new_client, is_primary=True)
        new_domain.save()

        return Response({"message": f"Client '{client_name}' created with subdomain: {client_name}.localhost"})