from django.db import models
from django.utils.timezone import now


class Application(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("declined", "Declined"),
    ]

    full_name = models.CharField(max_length=255)
    age = models.IntegerField()
    degree = models.CharField(max_length=255)
    job_experience = models.TextField()
    contact_time = models.TimeField()
    resume = models.FileField(upload_to="resumes/")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(default=now)  # ✅ Provide a default value

    def __str__(self):
        return f"{self.full_name} - {self.status}"



class ContactMessage(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.full_name}"
