# attendance/frontend_urls.py
from django.urls import path
from .views import check_page

urlpatterns = [
    path('check/', check_page, name='check_page'),
]
