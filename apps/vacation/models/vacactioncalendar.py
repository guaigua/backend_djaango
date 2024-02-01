from django.db import models
from apps.accounts.models import User
from apps.client.models import Client

class VacationCalendar(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    reason = models.TextField(blank=True)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ('client', 'start_date', 'end_date')
       
    def __str__(self):
        """Return a string representation."""
        return f"{self.client} - {self.status} - {self.start_date} to {self.end_date}"
