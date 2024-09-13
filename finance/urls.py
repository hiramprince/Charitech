from django.urls import path, include
from .views import home, about, contact, blog, course, donor, volunteer, dashboard, logout_view,login_view, signup_view

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
     path('signup/', signup_view, name='signup'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('course/', course, name='course'),
    path('donor/', donor, name='donor'),
    path('volunteer/', volunteer, name='volunteer'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
]
