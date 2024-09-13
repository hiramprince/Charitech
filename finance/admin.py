from django.contrib import admin
from .models import UserType, User

@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('UserTypeName', 'UserTypeDescription')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'UserType', 'UserContact', 'UserLocation', 'UserDepartment')
