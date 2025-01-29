from django.urls import path
<<<<<<< HEAD
from .views import RegisterView, LoginView, LogoutView
=======
from .views import *
>>>>>>> b0373d25bb767dadd04c84dda45f594e02c5d38e

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
<<<<<<< HEAD
]
=======
    path('profile/', ProfileView.as_view(), name='profile-detail'),
]
>>>>>>> b0373d25bb767dadd04c84dda45f594e02c5d38e
