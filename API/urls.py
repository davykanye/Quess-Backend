from .views import RegisterAPI
from django.urls import path
from knox import views as knox_views
from .views import *

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', Login, name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/encrypt/', encrypt_data, name='encrypt_data'),
    path('api/create_wallet/', create_wallet, name='create_wallet'),
    path('api/create_account/', create_account, name='create_account'),
    path('api/get_account/', get_account, name='get_account'),
    path('api/fund_wallet/', fund_wallet, name='fund_wallet'),
    path('api/get_wallet/', get_wallet, name='get_wallet'),
    path('api/charge_wallet/', charge_wallet, name='charge_wallet'),
    path('api/charge/', intialize_charge, name='charge_account'),
    path('api/complete/', complete_charge, name='complete_charge'),
]
