from django.db import models

class phones(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='images/')
    description = models.TextField()
    def __str__(self):
        return self.model
    
class noutbook(models.Model):
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='images/')
    description = models.TextField()
    def __str__(self):
        return self.model
    