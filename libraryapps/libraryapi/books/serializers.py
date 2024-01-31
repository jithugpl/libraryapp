from books.models import Book
from rest_framework import serializers
from django.contrib.auth.models import User

class bookserializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['id','title','author','price']

class userserializer(serializers.ModelSerializer):

    #password=serializers.CharField(write_only=True) #to hide password
    #to make password encrypted:-
    def create(self, validated_data):  #to make password encrypted
        u=User.objects.create(username=validated_data['username'])
        u.set_password(validated_data['password'])
        u.save()
        return u

    class Meta:
        model=User
        fields=['id','username','password']
