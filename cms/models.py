from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField

# Create category model.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    # description = models.TextField(max_length=250)
    description = RichTextField(config_name='awesome_ckeditor')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

# Create tag model.
class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    description = RichTextField(config_name='awesome_ckeditor')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

# Create post model.
class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    status = models.BooleanField()
    featured_photo = models.ImageField(upload_to = "featured_photos", null=True, blank=True)
    description = RichTextField(config_name='awesome_ckeditor')
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title