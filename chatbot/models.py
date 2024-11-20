from django.db import models

class CollegeInfo(models.Model):
    key = models.CharField(max_length=100, unique=True)  # Key to represent different information (e.g., 'establishment_date', 'courses')
    value = models.TextField()  # Value for the key (e.g., establishment date, courses offered, etc.)

    def __str__(self):
        return self.key
