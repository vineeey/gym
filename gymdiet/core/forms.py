from django import forms
from .models import DietPlan
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('trainer', 'Trainer'),
    )
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, initial='customer')

    class Meta:
        model = User
        fields = ['username', 'password', 'user_type']

class DietPlanForm(forms.ModelForm):
    class Meta:
        model = DietPlan
        fields = ['date', 'meals', 'calories', 'details']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'meals': forms.Textarea(attrs={'rows': 3}),
            'details': forms.Textarea(attrs={'rows': 3}),
        }