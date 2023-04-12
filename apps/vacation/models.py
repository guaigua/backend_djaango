from django.db import models

class Vacation(models.Model):
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE)
    days_total = models.IntegerField()
    days_used = models.IntegerField(default=0)

    def days_available(self):
        return self.days_total - self.days_used

    def __str__(self):
        return f"Vacation of {self.client}: {self.days_available()} days available"
