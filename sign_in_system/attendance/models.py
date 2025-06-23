from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.utils import timezone

class Attendance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField(default=timezone.now)
    check_out_time = models.DateTimeField(null=True, blank=True)
    date = models.DateField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'date')  # ✅ One attendance per user per day

    def __str__(self):
        return f"{self.user.username} - {self.date}"
