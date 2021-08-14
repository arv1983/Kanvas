from django.contrib import auth
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import status, serializers
from kanvas1.serializers import UserSerializer, LoginSerializer, CourseSerializer, CourseUpdateSerializer
from .permission import PermissionSuperUser, PermissionStaff
from kanvas1.models import Course

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



class CourseView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [PermissionSuperUser, PermissionStaff] 
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if Course.objects.filter(name=serializer.validated_data['name']).exists():
            return Response({'error': 'Course already exists'}, status=status.HTTP_409_CONFLICT)

        course = Course.objects.get_or_create(**serializer.validated_data)[0]
        print("course")
        serializer = CourseSerializer(course)
        print(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, course_id=''):
        print(course_id)
          





        course = get_object_or_404(Course, id=course_id)
        print(course.name)
        
        course.users = serializer.validated_data['users']

        course.save()

        serializer = CourseUpdateSerializer(course)
        return Response(serializer.data)
        








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

