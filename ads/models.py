# ads/models.py
from django.db import models
from users.models import User
from categories.models import Category
from locations.models import City

class Ad(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('moderation', 'Moderation'),
        ('rejected', 'Rejected'),
        ('sold', 'Sold'),
        ('active', 'Active'),
    )

    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    description = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    photos = models.ImageField(upload_to='ad_photos/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title

class AdModeration(models.Model):
    DECISION_CHOICES = (
        ('publish', 'Publish'),
        ('revision', 'Revision'),
    )

    moderation_date = models.DateTimeField(auto_now_add=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    moderator = models.ForeignKey(User, on_delete=models.CASCADE)
    decision = models.CharField(max_length=10, choices=DECISION_CHOICES)
    rejection_reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Moderation of {self.ad.title} by {self.moderator.username}"
