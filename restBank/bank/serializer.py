from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from bank.models import Bank


class BankModelSerializer(ModelSerializer):
    class Meta:
        model=Bank
        fields='__all__'


class BankLoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=50)
    password=serializers.CharField(max_length=50)