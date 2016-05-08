from __future__ import unicode_literals

from django.db import models

# Create category model.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name

# Create tag model.
class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name

# Create post model.
class Post(models.Model):
    title = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    status = models.BooleanField()
    featured_photo = models.ImageField(upload_to = "featured_photos")
    description = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title