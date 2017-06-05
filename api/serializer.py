from django.contrib.auth.models import User, Group

from rest_framework import serializers

from protoapp.models import Author, Quote

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    quotes = serializers.HyperlinkedRelatedField \
        (many=True, read_only=True, view_name='quote-detail')

    class Meta:
        model = Author
        fields = [ 'first_name', 'last_name', 'url', 'quotes' ]

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = [ 'name', 'url' ]

class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quote
        fields = [ 'author', 'text', 'url' ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [ 'email', 'groups', 'url', 'username' ]
