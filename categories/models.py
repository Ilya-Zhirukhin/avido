# categories/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    code = models.SlugField(unique=True)
    description = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    sort_order = models.IntegerField(default=0)

    def __str__(self):
        return self.name
