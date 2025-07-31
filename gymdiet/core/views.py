from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, DietPlanForm
from .models import Profile, DietPlan
from django.contrib.auth.models import User

def home_redirect(request):
    return redirect('signup')  # or 'login' or 'dashboard'

def home_view(request):
    return render(request, "core/home.html")

def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data.get('user_type', 'customer')
            # Check if username is taken
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already exists.')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password
                )
                Profile.objects.create(
                    user=user,
                    user_type=user_type
                )
                return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'core/login.html', {'error': 'Invalid credentials'})
    return render(request, 'core/login.html')

@login_required
def dashboard(request):
    profile = Profile.objects.get(user=request.user)
    if profile.user_type == 'trainer':
        # Trainers see all customers
        customers = Profile.objects.filter(user_type='customer')
        return render(request, 'core/trainer_dashboard.html', {'customers': customers})
    else:
        # Customers see their own diet plans
        diet_plans = DietPlan.objects.filter(user=request.user)
        return render(request, 'core/customer_dashboard.html', {'diet_plans': diet_plans})

@login_required
def assign_diet_plan(request, customer_id):
    profile = Profile.objects.get(user=request.user)
    if profile.user_type != 'trainer':
        return redirect('dashboard')
    customer = get_object_or_404(User, id=customer_id)
    # Only one diet plan per customer for simplicity; adjust if you want multiple plans per customer
    diet_plan = DietPlan.objects.filter(user=customer).first()
    if request.method == 'POST':
        form = DietPlanForm(request.POST, instance=diet_plan)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.trainer = request.user
            plan.user = customer
            plan.save()
            return redirect('dashboard')
    else:
        form = DietPlanForm(instance=diet_plan)
    return render(request, 'core/assign_diet_plan.html', {'form': form, 'customer': customer})

def logout_view(request):
    logout(request)
    return redirect('login')