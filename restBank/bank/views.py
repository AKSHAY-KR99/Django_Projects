from django.contrib.auth import authenticate, login, logout
from rest_framework import status, permissions
from rest_framework.authentication import TokenAuthentication

from .serializer import BankModelSerializer, BankLoginSerializer
from rest_framework.views import APIView
from .models import Bank
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
# Create your views here.

class BankList(APIView):

    def get(self,request):
        accounts=Bank.objects.all()
        serializer=BankModelSerializer(accounts,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=BankModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class BankDetails(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self,id):
        return Bank.objects.get(id=id)

    def get(self,request,id):
        bank=self.get_object(id)
        serializer=BankModelSerializer(bank)
        return Response(serializer.data)

    def put(self,request,id):
        bank=self.get_object(id)
        serializer=BankModelSerializer(bank,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        bank=self.get_object(id)
        bank.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BankLogin(APIView):
    def post(self,request):
        serializer=BankLoginSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data.get("username")
            password=serializer.validated_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                token,created=Token.objects.get_or_create(user=user)
                return Response({"token":token.key},status=status.HTTP_201_CREATED)


class LogoutApi(APIView):
    def get(self,request):
        logout(request)
        request.user.auth_token.delete()


