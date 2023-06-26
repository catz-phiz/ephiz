from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    description = models.TextField(blank=True, null = True)
    price = models.FloatField()
    isSold = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)

    
    def __str__(self):
        return self.name