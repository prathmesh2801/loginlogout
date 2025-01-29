from django.db import models

<<<<<<< HEAD
# Create your models here.
=======
# User model
>>>>>>> b0373d25bb767dadd04c84dda45f594e02c5d38e
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
<<<<<<< HEAD
    
    def __str__(self):
        return self.username
=======

    def __str__(self):
        return self.username

# Profile model linked to User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    location = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
>>>>>>> b0373d25bb767dadd04c84dda45f594e02c5d38e
