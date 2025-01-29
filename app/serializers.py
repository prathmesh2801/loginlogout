from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
<<<<<<< HEAD
        fields = ['id', 'username', 'password', 'email']
=======
        fields = ['id', 'username', 'password', 'email']


from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # This will return the username instead of the user ID

    class Meta:
        model = Profile
        fields = ['user', 'bio', 'profile_picture', 'location']
>>>>>>> b0373d25bb767dadd04c84dda45f594e02c5d38e
