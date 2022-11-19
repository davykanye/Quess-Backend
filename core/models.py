from django.db import models
# Create your models here.
from email.policy import default
from enum import unique
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser):
    username = models.CharField(unique=True, default=None, max_length=255)
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, null=True, blank=False)
    last_name = models.CharField(max_length=255, null=True, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email


class Wallet(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=False, null=False)
    amount = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return str(self.user)


class Transaction(models.Model):
    amount = models.IntegerField(blank=False, null=False)
    debitor = models.OneToOneField(
        Wallet, on_delete=models.CASCADE, blank=False, null=False)
    creditor = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=False, null=False)
    date_created = models.DateField(auto_now_add=True)


class Bank_Account(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=False, null=False)
    bank_name = models.CharField(max_length=255)
    account_number = models.IntegerField()