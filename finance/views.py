from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from finance.forms import UserRegistrationForm
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives, send_mail
# Ensure custom fields are handled through a separate model or UserProfile

# A form for custom user creation including extra fields
class CustomUserCreationForm(forms.ModelForm):
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput,
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

def home(request):
    return render(request, 'finance/charitechlogin.html')

def about(request):
    return render(request, 'finance/charitechabout.html')

def contact(request):
    return render(request, 'finance/charitechcontact.html')

def blog(request):
    return render(request, 'finance/charitechblog.html')

def course(request):
    return render(request, 'finance/charitechcourse.html')

def donor(request):
    return render(request, 'finance/donor.html')

def volunteer(request):
    return render(request, 'finance/volunteer.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def login_signup_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if action == 'signup':
            username = request.POST.get('username')
            user_department = request.POST.get('department', None)
            user_location = request.POST.get('location', None)

            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, email=email, password=password)
                # Save custom fields in a separate model or extend User
                # user.profile.department = user_department
                # user.profile.location = user_location
                user.save()
                login(request, user)
                messages.success(request, 'Account created successfully! Welcome')
                return redirect('donor')
            else:
                messages.error(request, 'Username already exists.')

        elif action == 'login':
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                # Assuming UserType is a custom field or related model
                # Redirect based on UserType
                if user.profile.user_type == 'Donor':
                    return redirect('donor')
                elif user.profile.user_type == 'Volunteer':
                    return redirect('volunteer')
                elif user.profile.user_type == 'Manager':
                    return redirect('dashboard')
            else:
                messages.error(request, 'Invalid credentials')

    return render(request, 'registration/login.html')


def signup_view(request):
    if request.method == 'POST':
        
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            email_html = get_template('Email/VerificationEmail.html')
            data = {'username':user_name}
            subject = 'Account verification'
            fromEmail = "hjatuhirwe@gmail.com"
            To = [email]
            content = email_html.render(data)
            message = EmailMultiAlternatives(subject,content,fromEmail,To)
            message.attach_alternative(content,'text/html')
            message.send()
        #     else:
        # form = UserRegistrationForm()
        return render(request, 'registration/signup.html',{'form':form})

def logout_view(request):
    django_logout(request)
    return redirect('home')
