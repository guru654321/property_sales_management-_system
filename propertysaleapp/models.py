from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField()
    message = models.TextField()

class ClientData(models.Model):
    client_name = models.CharField(max_length=255)
    client_login_id = models.CharField(max_length=255)
    client_password = models.CharField(max_length=255)
    client_confirm_password = models.CharField(max_length=255)
    client_gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    client_email = models.EmailField()
    client_number = models.CharField(max_length=15)
    client_DOB = models.DateField()
    client_address1 = models.CharField(max_length=255)
    client_address2 = models.CharField(max_length=255)
    client_city = models.CharField(max_length=100)
    client_state = models.CharField(max_length=100)
    client_country = models.CharField(max_length=100)
    client_picture = models.ImageField(upload_to='static/new_property_images/', blank=True)

class NewPropertyData(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('Apartment', 'Apartment'),
        ('Independent Floor', 'Independent Floor'),
        ('Builder Floor', 'Builder Floor'),
        ('Villa', 'Villa')
    ]

    STATUS_CHOICES = [
        ('Ready to Move', 'Ready to Move'),
        ('Resale', 'Resale'),
        ('Under Construction', 'Under Construction')
    ]

    seller_name = models.CharField(max_length=255,null=True)
    property_name = models.CharField(max_length=255)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    status_name = models.CharField(max_length=20, choices=STATUS_CHOICES)
    property_cost = models.DecimalField(max_digits=20, decimal_places=2)
    property_size = models.CharField(max_length=200)
    seller_contact_details = models.BigIntegerField()
    email_property = models.TextField(default='Default Amenities')
    property_amenities = models.TextField(default='Default Amenities', null=True)
    property_specifications = models.TextField(default='Default Amenities')
    property_total_rooms = models.PositiveIntegerField()
    property_balcony = models.CharField(max_length=200)
    property_total_bathrooms = models.PositiveIntegerField()
    property_address = models.TextField(default='Default Amenities')
    property_image = models.ImageField(upload_to='static/new_property_images/')
    property_description = models.TextField()

class NewPropertyTypeData(models.Model):
    seller_name = models.CharField(max_length=255,null=True)
    add_type_name=models.CharField(max_length=100)
    add_type_description=models.TextField()


class NewstatusData(models.Model):
    seller_name = models.CharField(max_length=255,null=True)
    status_name=models.CharField(max_length=100)
    status_description=models.TextField()
