from django.db import models
from datetime import timedelta
from django.utils import timezone


class Task(models.Model):
    name = models.CharField(max_length=50)
    last_completed = models.DateTimeField(default=timezone.now)
    frequency = models.IntegerField(default=45)

    def complete(self):
        self.last_completed = timezone.now()
        self.save()

    def time_remaining(self):
        time = timezone.now() - self.last_completed
        return int(self.frequency - divmod(time.total_seconds(), 60)[0])

    def print_remaining(self):
        mins = abs(self.time_remaining())
        if mins <= 1:
            return str(mins) + " minute"
        elif mins <= 60:
            return str(mins) + " minutes"
        elif mins <= 1440:
            return str("{:.1f}".format(mins / 60)) + " hours"
        else:
            return str("{:.1f}".format(mins / 1440)) + " days"

    def print_frequency(self):
        mins = self.frequency
        if mins <= 1:
            return str(mins) + " minute"
        elif mins <= 60:
            return str(mins) + " minutes"
        elif mins <= 1440:
            return str("{:.1f}".format(mins / 60)) + " hours"
        else:
            return str("{:.1f}".format(mins / 1440)) + " days"
