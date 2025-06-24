from django.urls import path
from .views import RegisterView, LoginView, register_view, welcome_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('welcome/', welcome_view, name='welcome'),
]

