from django.contrib.auth.hashers import make_password, check_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from wabTest.settings import SECRET_KEY
from account.models import Account
from uuid import uuid4
import jwt
import json

def authenticateAndReturnUserObject(request):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]
  
  token = request.headers["Authorization"]
  string_token = token.replace('Bearer ','')
  decoded_jwt = jwt.decode(string_token,SECRET_KEY,algorithms=['HS256'])
  user_id = decoded_jwt['user_id']
  
  user_object = Account.account_repository.filter(id=user_id,is_deleted=False).first()
  return user_object


