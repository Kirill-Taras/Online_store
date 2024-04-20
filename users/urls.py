from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterUserView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register')
]
