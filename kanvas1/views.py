from django.contrib import auth
from django.core.exceptions import ValidationError
from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import status, serializers
from kanvas1.serializers import UserSerializer, LoginSerializer

# Create your views here.
class UserView(APIView):
    def post(self, request):

        serializer = UserSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=serializer.validated_data['username']).exists():
            return Response({'error': 'email already exists'}, status=status.HTTP_409_CONFLICT)

        user = User.objects.create_user(**serializer.validated_data)
        print(user)
        serializer = UserSerializer(user)
        print(serializer)
        
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(**serializer.validated_data)
        
        if user:
            token = Token.objects.get_or_create(user=user)[0]
            return Response({'token': token.key})
        else:
            return Response({'Unauthorized': 'Failed to authenticate'}, status=status.HTTP_401_UNAUTHORIZED)
        

        # serializer = UserSerializer(data=request.data)

        # if not serializer.is_valid():
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # if User.objects.filter(username=serializer.validated_data('username')).exists():
        #     return Response({'erro': 'username already exists'}, status.HTTP_422_UNPROCESSABLE_ENTITY)


        # user = User.objects.create_user(**serializer.validated_data)
        # serializer_response = UserSerializer(user)
        # print(serializer_response)
        # return Response(serializer_response.data, status=status.HTTP_201_CREATED)



        # serializer = UserSerializer(data=request.data)
        
        # if not serializer.is_valid():
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # user = authenticate(**serializer.validated_data)
        
        # if user:
        #     token = Token.objects.get_or_create(user=user)[0]
        #     return Response({'token': token.key})
        # else:
        #     return Response({'Unauthorized': 'Failed to authenticate'}, status=status.HTTP_401_UNAUTHORIZED)

