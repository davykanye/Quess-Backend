from dataclasses import fields
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, LoginSerializer, RegisterSerializer, Bank_AccountSerializer, WalletSerializer
from django.contrib.auth import login
from .models import User, Wallet, Transaction, Bank_Account

import json
from django.views.generic.edit import CreateView
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

from datetime import datetime
# Register API


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        user = self.get_serializer(user)
        return Response({
            "user": RegisterSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
@api_view(['POST'])
def Login(request):
    user = User.objects.get(username=request.data['username'], password=request.data['password'])

    return Response({
            "user": RegisterSerializer(user, many=False).data,
            "token": AuthToken.objects.create(user)[1]
        })


'''
TRANSACTION AND BANKING VIEWS
    * intialize --- charge recipient account
    * complete --- submit otp, confirm payment and transfer to customer

    * Add Bank Account
    * Fund Wallet
'''

@ api_view(['POST'])
def fund_wallet(request):
    ''' posted data would be { "account_number": 2249996209, "amount":"100"} '''
    wallet = Wallet.objects.get(user=request.user)
    wallet.amount += int(request.data['amount'])
    wallet.save() # save
    return Response({"Deposit Successful":{'amount': wallet.amount}})

@ api_view(['GET'])
def get_account(request):
    ''' just auth token is needed '''
    bank = Bank_Account.objects.get(user=request.user)

    data = Bank_AccountSerializer(bank, many=False)

    return Response(data.data)

@ api_view(['POST'])
def create_account(request):
    ''' posted data would be { "account_number": 2249996209, "bank_name":"UBA", "date_of_birth": "10-12-2003"} '''
    bank_account = Bank_Account.objects.create(user=request.user,
    account_number=request.data['account_number'],
    bank_name=request.data['bank_name'])
    bank_account.save()
    data = Bank_AccountSerializer(bank_account, many=False)
    return Response({'Bank Account Created Successful': data.data})

@api_view(['POST'])
def encrypt_data(request):
    ''' (not working) posted data would be { "email": "customer@email.com",
      "amount": "10000",
      "bank": {
          code: "057",
          account_number: "0000000000"
      },
      "birthday": "1995-12-23"
    } '''
    # cipher = Cipher()
    # data = cipher.encrypt(json.dumps(request.data))
    info = b"bandom string"
    data = cipher.encrypt(info)
    return Response(data)


''' WALLET VIEWS '''


@ api_view(['POST'])
def create_wallet(request):
    ''' no params just call it with a auth token  '''
    wallet = Wallet.objects.create(user=request.user)
    wallet.save()
    data = WalletSerializer(wallet, many=False)
    return Response(data.data)


@api_view(['GET'])
def get_wallet(request):
    ''' no params just call it with a auth token  '''
    wallet = Wallet.objects.get(user=request.user)

    data = WalletSerializer(wallet, many=False)

    return Response(data.data)


@ api_view(['POST'])
def charge_wallet(request):
    ''' posted data would be something like{ "wallet": "email", "amount":"100"} '''
    try:
        debitor = Wallet.objects.get(user=request.user)
        creditor = Wallet.objects.get(user__email=request.data['wallet'])
        # transaction performed
        debitor.amount = debitor.amount + int(request.data['amount'])
        debitor.save()
        creditor.amount = creditor.amount - int(request.data['amount'])
        creditor.save()
        # transaction recorded and stored
        transaction = Transaction.objects.create(
            amount=int(request.data['amount']),
            debitor=debitor,
            creditor=creditor.user
        )
        transaction.save()
    except Exception as e:
        return Response(e)
    return Response("Wallet transaction Successful")


''' PAYSTACK VIEWS '''


@ api_view(['POST'])
def intialize_charge(request):
    ''' (not working) posted data would be  { "email": "customer@email.com", "amount": "10000", "bank": { "code": "057", "account_number": "0000000000" }, "birthday": "1995-12-23" } '''
    try:
        paystack.charge(request.data)
        return Response("Success")
    except Exception as e:
        return Response(e)


@ api_view(['POST'])
def complete_charge(request):
    ''' (not working) posted data would be { "otp": "123456", "reference": "5bwib5v6anhe9xa" } '''
    paystack = PayStackClient()  # sourcery skip: use-named-expression
    try:
        otp_response = paystack.submit_otp(request.data)
    except Exception as e:
        return Response(e)
    if otp_response['data']['status'] != 'success':
        return Response("Transaction pending")
    amount = otp_response['data']['amount']
    transfer_recipient = paystack.create_recipient(user_data)
    transfer_response = paystack.transfer(
        amount, transfer_recipient['data']["recipient_code"])
    if transfer_response:
        return Response("Transaction Completed")


@api_view(['POST'])
def User_Account(request):
    User_Account_data = JSONParser().parse(request)
    User_Account_serializer = User_AccountSerializer(data=User_Account_data)
    if User_Account_serializer.is_valid():
        User_Account_serializer.save()
        return JsonResponse(User_Account_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(User_Account_serializer.data, status=status.HTTP_400_BAD_REQUEST)
