from email.policy import default
from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='hook_a_book/media/images', null=True, blank=True, width_field=None, height_field=None)
    price = models.IntegerField()
    description = models.TextField()
