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
    users = UserSerializer(many=True, required=False)
    name = serializers.CharField(required=True)

class CourseUpdateSerializer(serializers.ListField):
    # id = serializers.IntegerField(read_only=True)
    user_ids = UserSerializer(required=True)


