from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from account import views

from account.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('github-login', GithubLogin.as_view()),
    path('signup', UserSignup.as_view()),
    path('login', UserLogin.as_view()),
    path('profile', EditProfile.as_view()),
    path('user/<int:id>', ViewProfile.as_view()),
    path('user/<int:id>', DeleteUser.as_view()),
]