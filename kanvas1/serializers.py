from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    is_staff = serializers.BooleanField(required=False)
    is_superuser = serializers.BooleanField(required=False)
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    users = UserSerializer(many=True, read_only=True)


class UserSimpleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()

class CourseGetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    users = UserSimpleSerializer(many=True, read_only=True)    



class CourseUpdateSerializer(serializers.Serializer):
    # name = serializers.CharField()
    users = User()


class UserSimples(serializers.Serializer):
    name = serializers.CharField()
    


class SubmissionsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    grade = serializers.IntegerField(required=False)
    repo = serializers.CharField(required=True)    

    user_id = serializers.IntegerField(read_only=True)
    activity_id = serializers.IntegerField(read_only=True)

    
class ActivitiesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    points = serializers.IntegerField(required=False)    
    submissions = SubmissionsSerializer(many=True, read_only=True)


class SubmissionGradeSerializer(serializers.Serializer):
    grade = serializers.IntegerField()







class CourseInsSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    users = UserSimpleSerializer(many=True, read_only=True)

