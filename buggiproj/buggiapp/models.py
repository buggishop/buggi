from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(models.Model):
    UserId=models.IntegerField(primary_key=True)
    FirstName= models.CharField(max_length=30)
    LastName= models.CharField(max_length=30)
    Password=models.CharField(max_length=255)
    Email_Id=models.EmailField(max_length=50)
    Phone=PhoneNumberField()
    last_active=models.DateField(auto_now=False, auto_now_add=False)
    user_type=models.CharField(max_length=5)
    email_verified=models.BooleanField()
    phone_verified=models.BooleanField()
    Buggy_point=models.IntegerField()


class Address_user(models.Model):
    UserId=models.ForeignKey(User,on_delete=models.CASCADE)
    Address= models.CharField(max_length=255)
    pincode= models.CharField(max_length=6)
    Contact_number=PhoneNumberField()
    Secondary_number=PhoneNumberField()
    
class Shop(models.Model):
    ShopId=models.IntegerField(primary_key=True)
    UserId=models.ForeignKey(User,on_delete=models.CASCADE)
    Shop_name=models.CharField(max_length=30)
    Shop_image=models.models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)

class Address_shop(models.Model):
    ShopId=models.ForeignKey(Shop,on_delete=models.CASCADE)
    Address= models.CharField(max_length=255)
    pincode= models.CharField(max_length=6)
    Contact_number=PhoneNumberField()
    Secondary_number=PhoneNumberField()