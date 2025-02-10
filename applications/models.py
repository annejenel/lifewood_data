from django.db import models

class Application(models.Model):
    full_name = models.CharField(max_length=255)
    age = models.IntegerField()
    degree = models.CharField(max_length=255)
    job_experience = models.TextField()
    contact_time = models.TimeField()
    resume = models.FileField(upload_to="resumes/")

    def __str__(self):
        return self.full_name


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.full_name}"
