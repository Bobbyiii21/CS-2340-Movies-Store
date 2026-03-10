from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from accounts.models import REGION_CHOICES

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/')
    def __str__(self):
        return str(self.id) + '-' + self.name

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_reported = models.BooleanField(db_default=False)
    def __str__(self):
        return str(self.id) + ' - ' + self.movie.name

class RegionalMovieStat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='regional_stats')
    region = models.CharField(max_length=50, choices=REGION_CHOICES)
    purchase_count = models.IntegerField(default=0)

    class Meta:
        unique_together = ('movie', 'region')

    def __str__(self):
        return f"{self.movie.name} – {self.region}: {self.purchase_count}"