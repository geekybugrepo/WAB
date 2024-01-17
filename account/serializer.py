from rest_framework import serializers
from account.models import Account
from account.github import Github

class GithubSerializer(serializers.Serializer):
  code = serializers.CharField(min_length=2,max_length=100)
  email = serializers.EmailField(required=False)
  id = serializers.IntegerField(required=False)
  # class Meta:
  #   fields = ['login', 'id', 'node_id', 'avatar_url', 'gravatar_id', 'url', 'html_url', 'followers_url', 'following_url', 'gists_url', 'starred_url', 'subscriptions_url', 'organizations_url', 'repos_url', 'email']
  def validate(self, data):
    code = data.get('code')
    access_token = Github.getTokenFromCode(code)
    if access_token:
      user_info = Github.getUserInfo(access_token)
      if user_info:
        user_emails = Github.getEmailData(access_token)
        data['email'] = next((email['email'] for email in user_emails if email['primary']), None)
        data['id'] = user_info.get('id')
        return data
      else:
        raise serializers.ValidationError({"message": "Invalid access token"})
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