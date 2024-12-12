from django.db import models

# Create your models here.


class Brend(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=250)
    photo = models.ImageField(upload_to="post/photos/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    brend = models.ForeignKey(Brend, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name