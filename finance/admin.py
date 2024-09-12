from django.contrib import admin
from . models import UserType, PaymentPlatform, Bank, Organization,User, Payment
# class UserAdmin(admin.ModelAdmin):
    # list_display = ('username', 'email',)

admin.site.register(UserType)
admin.site.register(PaymentPlatform)
admin.site.register(Bank)
admin.site.register(Organization)
admin.site.register(User)
admin.site.register(Payment)

# Register your models here.
