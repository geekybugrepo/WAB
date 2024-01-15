import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings

class Github:
  @staticmethod
  def getTokenFromCode(code):
    payload = {
      "client_id": settings.GITHUB_CLIENT_ID,
      "client_secret": settings.GITHUB_CLIENT_SECRET,
      "code": code
    }
    try:
      response = requests.post("https://github.com/login/oauth/access_token",headers={'Accept':'application/json'}, params=payload)
      response_payload = response.json()
      access_token = response_payload.get('access_token')
      return access_token
    except Exception as e:
      print(e)
      return Response({"message": "Invalid code"}, status=status.HTTP_400_BAD_REQUEST)


  @staticmethod
  def getUserInfo(access_token):
    try: 
      headers = {
        "Authorization": f"Bearer {access_token}"
      }
      response = requests.get("https://api.github.com/user",headers=headers)
      response_payload = response.json()
      return response_payload
    except Exception as e:
      print(e)
      return Response({"message": "Invalid access token"}, status=status.HTTP_400_BAD_REQUEST)
    