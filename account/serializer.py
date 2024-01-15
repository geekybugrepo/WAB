from rest_framework import serializers
from account.models import Account

class UserSignupSerializer(serializers.ModelSerializer):

  class Meta:
    model = Account
    fields = ['full_name', 'email', 'phone_number', 'address', 'gender', 'password']


class UserLoginSerializer(serializers.ModelSerializer):

  class Meta:
    model = Account
    fields = ['email', 'password']

class EditProfileSerializer(serializers.ModelSerializer):

  class Meta:
    model = Account
    fields = ['full_name', 'phone_number', 'address', 'gender']

class GetUserSerializer(serializers.ModelSerializer):

  class Meta:
    model = Account
    fields = ['full_name', 'email', 'phone_number', 'address', 'gender']