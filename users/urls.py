from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterUserView, ConfirmRegisterView, UserUpdateView, generate_new_password
from django.contrib.auth.views import LoginView, LogoutView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('confirm/', ConfirmRegisterView.as_view(), name='confirm'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/genpassword', generate_new_password, name='generate_new_password'),
]
