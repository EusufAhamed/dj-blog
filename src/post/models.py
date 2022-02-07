from django.db import models
from ckeditor.fields import RichTextField

from user.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_post')
    image = models.ImageField()
    description = RichTextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def pub_date_day(self):
        return self.pub_date.strftime('%d')

    def pub_date_mon(self):
        return self.pub_date.strftime('%b')