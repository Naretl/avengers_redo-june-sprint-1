"""
URL configuration for sign_in_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework.authtoken.views import obtain_auth_token  # ✅ Keep this

urlpatterns = [
    

    path('admin/', admin.site.urls),
    path('api/', include('attendance.urls')),                # ✅ Your attendance API
    path('api-token-auth/', obtain_auth_token),              # ✅ Token login endpoint
    path('api/users/', include('users.urls')),               # ✅ Your user routes
    path('accounts/', include('django.contrib.auth.urls')), 
    path('attendance/', include('attendance.frontend_urls')), 
    path('accounts/', include('users.urls')),
    path('attendance/', include('attendance.urls')),  # ✅ users.urls should have register_view etc.
 # 👈 for template views
 # ✅ Django login/logout views
]





