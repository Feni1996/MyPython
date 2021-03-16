from django.db import models

# Create your models here.
class feedback(models.Model):
    Name=models.CharField(max_length=10)
    Email = models.EmailField(max_length=20)
    Feedback = models.TextField(blank=True, null=True)
    Session = models.TextField(blank=True, null=True)
    Rating = models.DecimalField(decimal_places=2, max_digits=1000)

    def __str__(self):
        return self.Name

    
class Person(models.Model):
    Name = models.CharField(max_length=10)
    Email_id = models.EmailField(max_length=15)
    phone_number = models.IntegerField()
    Address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.Name
