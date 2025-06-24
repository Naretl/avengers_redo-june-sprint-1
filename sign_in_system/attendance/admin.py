from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'check_in_time', 'check_out_time')
    list_filter = ('date', 'user')
    search_fields = ('user__username',)

