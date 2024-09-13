from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User, UserType
from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login
from django.contrib.auth import get_user_model, login as django_login
from django.shortcuts import render, redirect


# Ensure custom fields are handled through a separate model or UserProfile
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
    return render(request, 'finance/dashboard.html')




def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']  # Email can still be collected but won't be used for authentication
        password = request.POST['password']
        password2 = request.POST['password2']
        account_type = request.POST['account_type']
        department = request.POST.get('department', '')
        location = request.POST.get('location', '')

        if password != password2:
            return render(request, 'registration/signup.html', {'error': 'Passwords do not match'})

        User = get_user_model()
        user = User.objects.create_user(username=username, email=email, password=password)

        # Assign user type and additional fields
        user.UserType, _ = UserType.objects.get_or_create(UserTypeName=account_type)
        if account_type == 'Volunteer':
            user.UserDepartment = department
            user.UserLocation = location
        user.save()

        django_login(request, user)
        if account_type == 'Donor':
            return redirect('donor')
        elif account_type == 'Volunteer':
            return redirect('volunteer')
        else:
            return redirect('dashboard')

    return render(request, 'registration/signup.html')





import logging
logger = logging.getLogger(__name__)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            django_login(request, user)
            user_type_name = getattr(user.UserType, 'UserTypeName', 'Unknown')
            logger.debug(f'Authenticated user {username} with UserTypeName: {user_type_name}')

            if user_type_name == 'Donor':
                return redirect('donor')
            elif user_type_name == 'Volunteer':
                return redirect('volunteer')
            elif user_type_name == 'Manager':
                return redirect('dashboard')
            else:
                logger.debug('UserTypeName does not match any known types')
                return redirect('home')
        else:
            logger.debug('Authentication failed')
            return render(request, 'registration/login.html', {'error': 'Invalid login credentials'})

    return render(request, 'registration/login.html')



def logout_view(request):
    django_logout(request)
    return redirect('home')
