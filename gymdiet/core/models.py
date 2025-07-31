from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('trainer', 'Trainer'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='customer')

    def __str__(self):
        return f"{self.user.username} ({self.user_type})"

class DietPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='diet_plans')
    trainer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_plans')
    date = models.DateField()
    meals = models.TextField()
    calories = models.PositiveIntegerField()
    details = models.TextField(blank=True)

    def __str__(self):
        return f"Diet Plan for {self.user.username} ({self.date})"