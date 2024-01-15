from rest_framework import serializers
from account.models import Account
from account.github import Github

class GithubSerializer(serializers.Serializer):
  code = serializers.CharField(min_length=2,max_length=100)

  def validate(self, data):
    code = data.get('code')
    access_token = Github.getTokenFromCode(code)
    if access_token:
      user_info = Github.getUserInfo(access_token)
      return user_info
    else:
      raise serializers.ValidationError({"message": "Invalid code"})

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