    
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    MIDDLE_NAME_MAX_LENGTH = 30
    ROLE_CHOICES = (
        ('admin', 'Administrator'),
        ('moderator', 'Moderator'),
        ('user', 'User'),
    )

    middle_name = models.CharField(max_length=MIDDLE_NAME_MAX_LENGTH, blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    preferred_call_time = models.CharField(max_length=255)
    status_choices = (
        ('blocked', 'Blocked'),
        ('active', 'Active'),
        ('pending', 'Pending Activation'),
    )
    status = models.CharField(max_length=10, choices=status_choices, default='pending')

    groups = models.ManyToManyField(
        Group,
        related_name='avido_custom_user_set_groups',  
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='avido_custom_user_set_permisions', 
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

