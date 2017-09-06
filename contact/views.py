# encoding:utf-8
from django.shortcuts import render
from util.viewset import ViewSet
from .models import  Contact
from .serializers import ContactSerializer
# Create your views here.
class ContactViewset(ViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    model_class = Contact

