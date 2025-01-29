from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']


from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # This will return the username instead of the user ID

    class Meta:
        model = Profile
        fields = ['user', 'bio', 'profile_picture', 'location']