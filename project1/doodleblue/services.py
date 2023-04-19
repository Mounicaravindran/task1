'''import dataclasses
from doodleblue.models import Wallet,Customer
from django.contrib.auth.models import User

def initialize_wallet(customer_xid):
    # To create wallet and push data to DB
    user = User.objects.create_user(customer_xid)
    customer = Customer.objects.create(user=user)
    wallet = Wallet.objects.create()
    wallet_obj = wallet()
    wallet_obj.id = customer_xid["id"]
    wallet_obj.name = ["name"]
    wallet_obj.save()'''