from django.contrib import admin
from django.urls import path

from account.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup', UserSignup.as_view()),
    path('login', UserLogin.as_view()),
    path('profile', EditProfile.as_view()),
    path('user/<int:id>', ViewProfile.as_view()),
    path('user/<int:id>', DeleteUser.as_view()),
]