
from django.contrib import auth
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import status, serializers
from kanvas1.serializers import UserSerializer, LoginSerializer, CourseSerializer, CourseGetSerializer, ActivitiesSerializer, SubmissionsSerializer, SubmissionGradeSerializer
from kanvas1.permission import Facilitador, Instrutor, Estudante2
from kanvas1.models import Course, Activity, Submission

# Create your views here.
class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=serializer.validated_data['username']).exists():
            return Response({'error': 'Username ja existe'}, status=status.HTTP_409_CONFLICT)


        user = User.objects.create_user(**serializer.validated_data)
        
        serializer = UserSerializer(user)
        
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

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
    permission_classes = [Instrutor] 
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # curso = Course.objects.filter(name=serializer.validated_data['name']):
        # serializer = CourseSerializer(curso)
        # return Response(serializer.data, status=status.HTTP_200_OK)

        course = Course.objects.get_or_create(**serializer.validated_data)[0]
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def put(self, request, course_id):
        # course = get_object_or_404(Course, id=course_id)
        try:
            course = Course.objects.get(id=course_id)
        except:
            return Response({'errors': 'invalid course_id'}, status=status.HTTP_404_NOT_FOUND)


        for users in request.data['user_ids']:
            try:
                res = User.objects.get(id=users)
            except:
                return Response({"errors": "invalid user_id list"}, status=status.HTTP_404_NOT_FOUND)
            if res.is_staff | res.is_superuser:
                return Response({"errors": "Only students can be enrolled in the course."}, status=status.HTTP_400_BAD_REQUEST)

        course.users.set(request.data['user_ids'])
        course.save()
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def get(self, request, course_id=''):
        print(course_id)

        if course_id:
            try:
                get_course = Course.objects.get(id=course_id)
                serializer = CourseGetSerializer(get_course)
            except:
                return Response({"errors": "invalid course_id"}, status=status.HTTP_404_NOT_FOUND)
        
        else:
            get_course = Course.objects.all()
            serializer = CourseGetSerializer(get_course, many=True)
        
        return Response(serializer.data)
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [Instrutor]
    def delete(self, request, course_id):
        try:
            get_course = Course.objects.get(id=course_id)
        except:
            return Response({"errors": "invalid course_id"}, status=status.HTTP_404_NOT_FOUND)

        get_course.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



class ActivitiesView(APIView):


    permission_classes = [ Facilitador | Instrutor | Estudante2 ]  
    def get(self, request):
        # return Response({'d':'s'})
        current_user = request.user
        # if not current_user.is_staff and not current_user.is_superuser:

        
        try:
            # if not current_user.is_staff and not current_user.is_superuser:
            #     get_activitie = Activity.objects.get(id=current_user.id)
            # else:
            #     get_activitie = Activity.objects.all()
            get_activitie = Activity.objects.all()
        
        except:
            return Response({"erros": "nao existe atividades"}, status=status.HTTP_403_FORBIDDEN)

        print(get_activitie.__dict__)
        serializer = ActivitiesSerializer(get_activitie, many=True)

        return Response(serializer.data)





    authentication_classes = [TokenAuthentication] 
    permission_classes = [ Facilitador | Instrutor ]  
    def post(self, request):
        # return Response({'ss':'ss'})
        serializer = ActivitiesSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if Activity.objects.filter(title=serializer.validated_data['title']).exists():


            ss = Activity.objects.filter(title=serializer.validated_data['title'])[0]           
            print(ss.points)
            ss.points = request.data['points']
            ss.save()
            serializer = ActivitiesSerializer(ss)
            serializer.data['points']
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.validated_data['points'])
        activitie = Activity.objects.get_or_create(**serializer.validated_data)[0]
        serializer = ActivitiesSerializer(activitie)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        # mudar somente o grade se ja existir










          






class StudentActivitiesView(APIView):


    authentication_classes = [TokenAuthentication]  
    permission_classes = [ Facilitador | Instrutor | Estudante2]  
    def get(self, request):

        current_user = request.user
        print(current_user.is_staff)
        # try: 
        #     if not current_user.is_staff and not current_user.is_superuser:
        # get_submission = Submission.objects.get(user_id=current_user.id)
        # serializer = SubmissionsSerializer(get_submission)
        #     else:
        print('+++++++++++++++++++++++++++++')
        print(current_user.id)
        if current_user.is_staff | current_user.is_superuser:
            print('aqu')
            get_submission = Submission.objects.all()
            serializer = SubmissionsSerializer(get_submission, many=True)
        else:
            get_submission = Submission.objects.filter(user_id=current_user.id)
            serializer = SubmissionsSerializer(get_submission, many=True)


        return Response(serializer.data)





    permission_classes = [ Estudante2 ]  
    authentication_classes = [TokenAuthentication]  
    def post(self, request, activitie_id):
        # request.data['grade'] = null=True
        atividade = Activity.objects.get(id=activitie_id)
        serializer = SubmissionsSerializer(data=request.data)
        
        if not serializer.is_valid():   
            return Response({'deu': 'merda'})
        
        serializer.validated_data['grade'] = None
        course = Submission.objects.create(**serializer.validated_data, user=request.user, activity=atividade)
        serializer = SubmissionsSerializer(course)
        return Response(serializer.data, status=status.HTTP_201_CREATED) 

  
class EditaNotaView(APIView):
    authentication_classes = [TokenAuthentication]  
    permission_classes = [ Facilitador | Instrutor ]  
    def put(self, request, submission_id):
        
        try:
            submission = Submission.objects.get(id=submission_id)

        except:
            Response({"errors": "Invalid submission_id"})
        

        
        serializer = SubmissionGradeSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        submission.grade = serializer.validated_data['grade']
        submission.save()
        

        serializer = SubmissionsSerializer(submission)

        return Response(serializer.data, status=status.HTTP_200_OK)
