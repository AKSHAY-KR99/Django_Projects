from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework import mixins, generics, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authtoken
from rest_framework.authtoken.models import Token

from .models import AccountCreation
from .serializer import UserRegistrationSerializer, AccountCreationSerializer, LoginSerializer,DepositSerializer,WithdrawSerializer


# Create your views here.


class UserregistrationMixin(mixins.CreateModelMixin,generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class BankAccountCreationMixin(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AccountCreationSerializer
    def get(self,request):
        acnt = AccountCreation.objects.last()
        if acnt:
            lastaccno=acnt.accno
            lastaccno+=1
        else:
            lastaccno =1000
        acnt.accno=lastaccno
        account=AccountCreation.objects.get(accno=lastaccno)
        serializer=AccountCreationSerializer(account)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)



class BalanceCheck(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,accno):
        acnt=AccountCreation.objects.get(accno=accno)
        serializer=AccountCreationSerializer(acnt)
        return Response(serializer.data)




class BankLogin(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")
            user = authenticate(request, username=username, password=password)
            # user=AccountCreation.objects.get(username=username)
            if user:
                login(request, user)
                print(user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key}, status=status.HTTP_200_OK)
            else:
                print("error")
                return Response(serializer.errors)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            # csrf token : bf52f8fecc8dbaa2319abfaf74f48f8cea8cf50f

class LogoutApi(APIView):
    def get(self,request):
        logout(request)
        request.user.auth_token.delete()


class WithdrawApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,accno):
        serializer=WithdrawSerializer(data=request.data)
        account=AccountCreation.objects.get(accno=accno)
        if serializer.is_valid():
            amount=serializer.validated_data.get("amount")
            if amount<account.balance:
                account.balance-=amount
                account.save()
                print(account.balance,account.username)
                return Response({"message":"Debited Successfully","balance":account.balance},status=status.HTTP_200_OK)
            else:
                return Response({"message":"Insuffient balance"})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DepositApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,accno):
        serializer=DepositSerializer(data=request.data)
        account=AccountCreation.objects.get(accno=accno)
        if serializer.is_valid():
            amount=serializer.validated_data.get("amount")
            account.balance+=amount
            account.save()
            print(account.balance,account.username)
            return Response({"message":"Amount Credited Succesfully","balance":account.balance},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
