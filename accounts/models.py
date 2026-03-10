from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

REGION_CHOICES = [
    ('northamerica', 'North America'),
    ('southamerica', 'South America'),
    ('europe',   'Europe'),
    ('asia', 'Asia'),
    ('australia',      'Australia'),
    ('africa', 'Africa'),
]

class UserProfile(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    region = models.CharField(max_length=50, choices=REGION_CHOICES, default='')

    def __str__(self):
        return f"{self.user.username} – {self.region}"