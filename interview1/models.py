from django.db import models

class Location(models.Model):
    pincode=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    lat=models.DecimalField(max_digits=6, decimal_places=4, null=True)
    lng=models.DecimalField(max_digits=6, decimal_places=4, null=True)
    accuracy=models.IntegerField(null=True, default=0)


    def __str__(self):
        return self.pincode

# Create your models here.
