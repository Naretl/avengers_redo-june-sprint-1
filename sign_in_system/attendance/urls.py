from django.urls import path
from .views import CheckInView, CheckOutView, check_page, staff_dashboard

urlpatterns = [
    path('check-in/', CheckInView.as_view(), name='api_check_in'),     # ✅ Changed name
    path('check-out/', CheckOutView.as_view(), name='api_check_out'),  # ✅ Changed name
    path('check/', check_page, name='check_page'),
    path('dashboard/', staff_dashboard, name='staff_dashboard'),
]



