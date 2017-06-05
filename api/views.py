from django.contrib.auth.models import Group, User
from django.shortcuts import render

from rest_framework import viewsets

from api.serializer \
     import AuthorSerializer, GroupSerializer, QuoteSerializer, UserSerializer
from protoapp.models import Author, Quote

class AuthorViewSet(viewsets.ModelViewSet):
    '''API endpoint that allows authors to be viewed or edited.'''
    queryset = Author.objects.all().order_by('last_name', 'first_name')
    serializer_class = AuthorSerializer

class GroupViewSet(viewsets.ModelViewSet):
    '''API endpoint that allows groups to be viewed or edited.'''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class QuoteViewSet(viewsets.ModelViewSet):
    '''API endpoint that allows quotes to be viewed or edited.'''
    queryset = Quote.objects.all().order_by('id')
    serializer_class = QuoteSerializer

class UserViewSet(viewsets.ModelViewSet):
    '''API endpoint that allows users to be viewed or edited.'''
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
