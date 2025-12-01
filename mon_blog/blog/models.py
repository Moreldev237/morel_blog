from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    images= models.ImageField(upload_to='posts/', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    
    def publish(self):
        self.published_date = timezone.now()
        self.is_published = True
        self.save()
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'