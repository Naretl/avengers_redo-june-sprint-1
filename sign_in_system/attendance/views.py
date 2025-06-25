from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from urllib.parse import urlencode

from .models import Attendance

@method_decorator(login_required, name='dispatch')
class CheckInView(View):
    def post(self, request):
        user = request.user
        today = timezone.now().date()

        if Attendance.objects.filter(user=user, date=today).exists():
            message = "Already checked in today."
        else:
            Attendance.objects.create(
                user=user,
                check_in_time=timezone.now(),
                date=today
            )
            message = "Checked in successfully!"

        return redirect(f'/attendance/check/?{urlencode({"message": message})}')


@method_decorator(login_required, name='dispatch')
class CheckOutView(View):
    def post(self, request):
        user = request.user
        today = timezone.now().date()

        try:
            attendance = Attendance.objects.get(user=user, date=today, check_out_time__isnull=True)
            attendance.check_out_time = timezone.now()
            attendance.save()
            message = "Checked out successfully!"
        except Attendance.DoesNotExist:
            message = "No check-in record found for today or already checked out."

        return redirect(f'/attendance/check/?{urlencode({"message": message})}')


@login_required
def check_page(request):
    user = request.user
    today = timezone.now().date()
    attendance = Attendance.objects.filter(user=user, date=today).first()
    message = request.GET.get('message')
    
    history = Attendance.objects.filter(user=user).order_by('-date')[:10]

    return render(request, 'attendance/check.html', {
        'attendance': attendance,
        'user': user,
        'history': history,
        'message': message 
    })

from django.contrib.auth.decorators import user_passes_test
from django.db.models import Count

def is_staff(user):
    return user.is_authenticated and user.user_type == 'staff'

@user_passes_test(is_staff)
def staff_dashboard(request):
    today = timezone.now().date()

    total_checkins_today = Attendance.objects.filter(date=today, check_in_time__isnull=False).count()
    total_checkouts_today = Attendance.objects.filter(date=today, check_out_time__isnull=False).count()
    total_users = Attendance.objects.values('user').distinct().count()

    attendance_by_day = Attendance.objects.extra({'day': "date(date)"}).values('day').annotate(count=Count('id'))

    context = {
        'total_checkins_today': total_checkins_today,
        'total_checkouts_today': total_checkouts_today,
        'total_users': total_users,
        'attendance_by_day': attendance_by_day,
    }
    return render(request, 'attendance/staff_dashboard.html', context)






