from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Application(models.Model):

    STATUS_CHOICES = [
        ('AP', 'Applied'),
        ('IN', 'Interview'),
        ('OF', 'Offer'),
        ('RJ', 'Rejected')
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='applications'
    )

    company_name = models.CharField(max_length=200)
    position_title = models.CharField(max_length=200)

    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='AP'
    )

    applied_date = models.DateField()
    interview_date = models.DateField(blank=True, null=True)

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def status_class(self):
        return {
            "A": "applied",
            "I": "interview",
            "O": "offer",
            "R": "rejected"
        }.get(self.status, "")

    def __str__(self):
        return f"{self.company_name} - {self.position_title}"
