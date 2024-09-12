from django.db import models
from django.contrib.auth.models import AbstractUser

class UserType(models.Model):
    UserTypeID = models.AutoField(primary_key=True)
    UserTypeName = models.CharField(max_length =100)
    UserTypeDescription = models.TextField()

    def __str__(self):
        return self.UserTypeName     

class PaymentPlatform(models.Model):
    PaymentPlatformId = models.AutoField(primary_key=True)
    PaymentPlatformName = models.CharField(max_length = 100)
    PaymentPlatformDescription = models.TextField()

    def __str__(self):
        return self.PaymentPlatformName  

class Bank(models.Model):
    BankID = models.AutoField(primary_key=True)
    BankName = models.CharField(max_length = 100)
    BankAccountNo = models.CharField(max_length = 25)
    BankBranch = models.CharField(max_length =100)

    def __str__(self):
        return f"{self.BankName}-{self.BankBranch}"  


class Organization(models.Model):
    OrganizationID = models.AutoField(primary_key=True)
    OrganizationName = models.CharField(max_length =100)
    OrganizationLocation = models.CharField(max_length = 100)
    Banks = models.ManyToManyField(Bank)

    def __str__(self):
        return {self.OrganizationName}

class User(AbstractUser):
    USERID = models.AutoField(primary_key=True)
    UserContact = models.CharField(max_length=100)
    UserLocation = models.CharField(max_length =100,null =True, blank = True)
    UserDepartment = models.CharField(max_length=100,null=True, blank = True)
    UserType = models.ForeignKey(UserType, on_delete=models.CASCADE)
    UserBank = models.ManyToManyField(Bank)
    Organizations = models.ManyToManyField(Organization)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='finance_user_set',
        blank =True,
        verbose_name ='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name ='finance_user_permissions_set',
        blank=True,
        verbose_name='user permission',
    )

    def save(self, *args, **kwargs):
        if not self.UserDepartment and not self.UserLocation:
            donor_type, created = UserType.objects.get_or_create(UserTypeName ='Donor')
            self.UserType =donor_type

        else: 
            volunteer_type, created = UserType.objects.get_or_create(UserTypeName= 'Volunteer')
            self.UserType = volunteer_type

        super(User, self).save(*args, **kwargs)
    def __str__(self):
        return self.username  

class Payment(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    PaymentAmount = models.DecimalField(max_digits=10, decimal_places=3)
    PaymentDescription = models.TextField()
    PaymentPlatform = models.ForeignKey(PaymentPlatform, on_delete=models.CASCADE)
    Banks = models.ForeignKey(Bank, on_delete=models.CASCADE)
    Users = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.PaymentAmount}-{self.PaymentPlatform.PaymentPlatformName}"  


