from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import AccountCreation


class UserRegistrationSerializer(ModelSerializer):
    class Meta:
        model= User
        fields=['first_name','last_name','username','password']

class AccountCreationSerializer(ModelSerializer):
    class Meta:
        model=AccountCreation
        fields='__all__'


class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()


class WithdrawSerializer(serializers.Serializer):
    amount=serializers.IntegerField()


class DepositSerializer(serializers.Serializer):
    amount=serializers.IntegerField()