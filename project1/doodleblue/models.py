from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    id=models.IntegerField(max_length=10, primary_key=True)
    owned_by=models.CharField(max_length=50)
    status=models.BooleanField(default=False)
    enabled_at=models.DateTimeField()
    balance=models.FloatField(max_length=20,default=0)

class Transactions(models.Model):
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE)
    #transaction_type=models.CharField(choices=["Deposit","Withdrawal"])
    amount=models.FloatField(max_length=20)
    transacted_at=models.DateTimeField(auto_now_add=True)
    
