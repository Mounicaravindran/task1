from django.urls import path
#from rest_framework.authtoken.views import obtain_auth_token
from doodleblue.views import EnableWallet,WalletBalance,WalletTransactions,AddMoney,Usemoney,Disablewallet,CustomAuthTokenLogin
urlpatterns = [
    #path('login/',views.CustomAuthTokenLogin.as_view)

    path('api-token-auth/', CustomAuthTokenLogin.as_view(), name='api_token_auth'),
    #path('init/', WalletInitView.as_view(), name='wallet_init'),
    path('enable-wallet/', EnableWallet.as_view(), name='enable_wallet'),
    path('view-balance/', WalletBalance.as_view(),name='view_balance'),
    path('view-transactions/',WalletTransactions.as_view(),name='view_transactions'),
    path('add-money/',AddMoney.as_view(),name='add_money'),
    path('withdraw-money/',Usemoney.as_view(),name='withdraw_money'),
    path('disable-wallet/',Disablewallet.as_view(),name='disable_wallet'),


]