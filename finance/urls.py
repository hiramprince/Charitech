from django.urls import path
from .views import home, about, contact, blog, course, donor, volunteer, dashboard, login_signup_view, logout_view,signup_view

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('course/', course, name='course'),
    path('donor/', donor, name='donor'),
    path('volunteer/', volunteer, name='volunteer'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', login_signup_view, name='login_signup'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
]
