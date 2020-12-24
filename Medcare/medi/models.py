from django.db import models

# Create your models here.
class Doctor(models.Model):
    CATEGORY = (
        ('Cardiology','Cardiology'),
        ('Neorology','Neorology'),
        ('Nephrology','Nephrology'),
        ('Medicine', 'Medicine'),
        ('Dermatology','Dermatology'),
        ('Neorosurgery','Neorosurgery'),
        ('Cardiacsurgery','Cardiacsurgery'),
        ('ENT','ENT',)
    )
    name = models.CharField(max_length = 200, null=True)
    phone = models.CharField(max_length = 200, null=True)
    category = models.CharField(max_length = 200, null=True, choices = CATEGORY)
    address = models.CharField(max_length = 200, null=True)

    def __str__(self):
        return self.name