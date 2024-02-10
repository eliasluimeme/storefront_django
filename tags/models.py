from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Tag(models.Model):
    label = models.CharField(max_length=255)

class TagedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # Type (Product, video, article) to find the table
    # ID to find the record
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) # ContentType is a model that represents the type of an object in our app
    object_id = models.PositiveIntegerField() # Referencing that particular object
    content_object = GenericForeignKey() # The actual object