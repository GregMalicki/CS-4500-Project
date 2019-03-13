from django.db import models
from datetime import timedelta
from django.utils import timezone


class Task(models.Model):
    name = models.CharField(max_length=50)
    last_completed = models.DateTimeField(default=timezone.now)
    frequency = models.IntegerField(default=45)

    def complete(self):
        self.last_completed = timezone.now

    def time_remaining(self):
        time = timezone.now() - self.last_completed
        return divmod(time.total_seconds(), 60)[0]
