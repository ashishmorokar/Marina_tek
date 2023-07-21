from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    description = models.TextField()
    genre = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return self.title
