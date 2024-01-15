from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.models import Account
from account.serializer import UserLoginSerializer, UserSignupSerializer, EditProfileSerializer, GetUserSerializer
from wabTest.authentication import authenticateAndReturnUserObject
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserSignup(APIView):
  def post(self, request):
    user_data = UserSignupSerializer(data=request.data)
    if user_data.is_valid():
      email_already_exists = Account.account_repository.filter(email=request.data['email'], is_deleted=False).first()
      if email_already_exists:
        return Response({"message": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)
      
      account_signup = Account(**user_data.validated_data)
      enc_pas = make_password(request.data['password'])
      account_signup.password = enc_pas
      account_signup.is_active = True
      
      try:
        account_signup.save()
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
      except:
        return Response({"message": "User creation failed", "data": user_data.errors}, status=status.HTTP_400_BAD_REQUEST)
    else:
      return Response({"message": "User creation failed", "data": user_data.errors}, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
  def post(self, request):
    user_data = UserLoginSerializer(data=request.data)
    if user_data.is_valid():
      account_exist = Account.account_repository.filter(email=request.data['email'], is_deleted=False).first()
      if not account_exist:
        return Response({"message": "User does not exists"}, status=status.HTTP_400_BAD_REQUEST)

      if check_password(request.data['password'], account_exist.password):
        try:
          refresh = RefreshToken.for_user(account_exist)
          return Response({
                            'refresh': str(refresh), 'access': str(refresh.access_token),
                            'message': 'Account successfully logged in'
                        }, status=status.HTTP_200_OK)
        except:
          return Response({"message": "User login failed", "data": user_data.errors}, status=status.HTTP_400_BAD_REQUEST)
      else:
        return Response({"message": "Invalid Password", "data": user_data.errors}, status=status.HTTP_400_BAD_REQUEST)

class ViewProfile(APIView):
  def get(self, request, id):
    user_object = authenticateAndReturnUserObject(request)
    if not user_object:
      return Response({'message': 'This user does not exists!'}, status=status.HTTP_403_FORBIDDEN)
    else:
      account_object = Account.account_repository.filter(id=user_object.id).first()
      if account_object and account_object.id == id:
        user_data = GetUserSerializer(account_object)

        return Response({"message": "User details fetched successfully", "data": user_data.data}, status=status.HTTP_200_OK)
      else:
        return Response({"message": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
      

class EditProfile(APIView):
  def put(self, request):
    user_object = authenticateAndReturnUserObject(request)
    if not user_object:
      return Response({'message': 'This user does not exists!'}, status=status.HTTP_403_FORBIDDEN)
    else:
      user_data = EditProfileSerializer(data = request.data)
      if user_data.is_valid():
        account_object = Account.account_repository.filter(id=user_object.id).first()
        if account_object:
          account_object.full_name = request.data['full_name']
          account_object.phone_number = request.data['phone_number']
          account_object.address = request.data['address']
          account_object.gender = request.data['gender']
          try:
            account_object.save()
            return Response({"message": "User updated successfully"}, status=status.HTTP_201_CREATED)
          except:
            return Response({"message": "User updation failed", "data": user_data.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
          return Response({"message": "User updation failed", "data": user_data.errors}, status=status.HTTP_400_BAD_REQUEST)
      else:
        return Response({"message": "User updation failed", "data": user_data.errors}, status=status.HTTP_400_BAD_REQUEST)        

class DeleteUser(APIView):
  def delete(self, request, id):
    user_object = authenticateAndReturnUserObject(request)
    if not user_object:
      return Response({'message': 'This user does not exists!'}, status=status.HTTP_403_FORBIDDEN)
    else:
      account_object = Account.account_repository.filter(id=user_object.id).first()
      if account_object:
        if account_object.id != id:
          return Response({'message': 'This user does not exists!'}, status=status.HTTP_403_FORBIDDEN)
        else:
          account_object.is_deleted = True
        try:
          account_object.save()
          return Response({"message": "User deleted successfully"}, status=status.HTTP_200_OK)
        except:
          return Response({"message": "User deletion failed"}, status=status.HTTP_400_BAD_REQUEST)
      else:
        return Response({"message": "User deletion failed"}, status=status.HTTP_400_BAD_REQUEST)