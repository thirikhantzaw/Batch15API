from django.db import models
import uuid
# Create your models here.

class Category(models.Model):
    id= models.UUIDField(editable=False, primary_key=True , default=uuid.uuid4)
    name = models.CharField(unique=True, max_length=200)
    image = models.ImageField(upload_to='Category')

    def __str__(self):
        return self.name
    
class Banner(models.Model):
    id= models.UUIDField(editable=False, primary_key=True , default=uuid.uuid4)
    name = models.CharField(unique=True, max_length=200)
    image = models.ImageField(upload_to='Banner')

    def __str__(self):
        return self.name