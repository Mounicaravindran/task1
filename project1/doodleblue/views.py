'''from django.shortcuts import render
from doodleblue.serializers import IntializeWalletSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
#from doodleblue.models import Wallet
# Create your views here.


class WalletInitView(APIView):
    #authentication_classes=[authentication.TokenAuthentication]
   # permission_classes=[permissions.IsAuthenticated]
    def post(self,request):
        user=request.user
        #wallet=Wallet.objects.create(wallet)
        serializer=IntializeWalletSerializer(wallet)
        return Response(serializer.data)

'class InitializeWallet(APIView):
    serializer_class = IntializeWalletSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            return_data = initialize_wallet(serializer.validated_data['customer_xid'])'''



from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework import generics,permissions,status
from rest_framework.views import APIView
from doodleblue.models import Wallet,Transactions
from doodleblue.serializers import WalletSerializer,TransactionSerializer
from django.contrib.auth.models import User



user=User.objects.create_user("john","john@gmail.com","john00")
user.save()

@authentication_classes((TokenAuthentication))
@permission_classes((IsAuthenticated))

class CustomAuthTokenLogin(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user'] 
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    
class EnableWallet(APIView):
    permission_classes= [permissions.IsAuthenticated]

    def post(self,request):
        wallet=Wallet.objects.get(user=request.user)
        return Response({'status':'enabled'})
    
class WalletBalance(APIView):
    permission_classes= [permissions.IsAuthenticated]

    def get(self,request):
        wallet=Wallet.objects.get(user=request.user)
        serializer=WalletSerializer(wallet)
        return Response(serializer.data)
    
class WalletTransactions(APIView):
    permission_classes= [permissions.IsAuthenticated]

    def get(self,request):
        wallet=Wallet.objects.get(user=request.user)
        transactions=Transactions.objects.filter(wallet=wallet)
        serializer=TransactionSerializer(transactions, many=True)
        return Response(serializer.data)
    
class AddMoney(APIView):
    permission_classes= [permissions.IsAuthenticated]

    def post(self,request):
        wallet= Wallet.objects.get(user=request.user)
        amount= request.data['amount']
        wallet.balance +=amount
        wallet.save()
        transaction = Transactions(wallet=wallet,amount=amount)
        transaction.save()
        return Response({'status':'success'})
    
class Usemoney(APIView):
    permission_classes= [permissions.IsAuthenticated]

    def post(self,request):
        wallet= Wallet.objects.get(user=request.user)
        amount=request.data['amount']
        if wallet.balance < amount:
            return Response({'status':'Insufficient Balance'})
        wallet.balance -= amount
        wallet.save()
        transaction =Transactions(wallet=wallet,amount=-amount)
        transaction.save()
        return Response({'status':'success'})
    
class Disablewallet(APIView):
    permission_classes= [permissions.IsAuthenticated]

    def get(self,request):
        wallet=Wallet.objects.get(user=request.user)
        wallet.delete()
        return Response({'status':'Disabled'})










    

