
from django.db import models
from django.contrib.auth.models import AbstractUser

class Car(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cars/')

   

class Medicine(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    from django.db import models


   




class Account(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    mobile = models.CharField(max_length=15)

    class Meta:
        managed = False  # Important! Don't let Django manage this table
        db_table = 'account'
        
        
        # myapp/models.py
from django.db import models

class UserProfile(models.Model):  # Renamed from Account
    mobile = models.CharField(max_length=10, unique=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.mobile
  # Matches the MySQL table name

  # otpapp/models.py
from django.db import models

class OTPModel(models.Model):
    mobile = models.CharField(max_length=15)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)




class Profile(models.Model):
    address = models.TextField(blank=True, null=True)
    health_details = models.TextField(blank=True, null=True)
    preferences = models.TextField(blank=True, null=True)


from django.db import models

class Prescription(models.Model):
    patient_name = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    symptoms = models.TextField()
    recommended_lab_test = models.TextField()
    extracted_medicines = models.TextField()
    uploaded_image = models.ImageField(upload_to='prescriptions/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} ({self.created_at})"

from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)



class Complaint(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    order_id = models.CharField(max_length=100)
    issue = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.order_id}"
    
  


from django.db import models

class CallBackRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, default='0000000000')
    preferred_time = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"
# models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Ensures no duplicate category names

    def __str__(self):
        return self.name

class Medicines(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="medicines")
    available = models.BooleanField(default=True)  # new field
    alternatives = models.ManyToManyField('self', symmetrical=False, blank=True)  # new field
    def __str__(self):
        return self.name

# models.py
# yourapp/models.py


class Tablet(models.Model):
    name = models.CharField(max_length=100)
    composition = models.TextField()
    dosage = models.TextField()
    side_effects = models.TextField()
   

    def __str__(self):
        return self.name

        from django.db import models

class MedicineInfo(models.Model):
    name = models.CharField(max_length=100)
    requires_prescription = models.BooleanField(default=False)

    def __str__(self):
        return self.name

        from django.db import models

class MedicineInstru(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.TextField()
    warnings = models.TextField()

    def __str__(self):
        return self.name

        return f"{self.user.username} - {self.medicine.name}"


from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    test_value = models.FloatField()  # ✨ Add test result value
    report_file = models.FileField(upload_to='reports/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.test_name}"

class Speciality(models.Model):
    test_name = models.CharField(max_length=100)  # like 'TSH'
    min_value = models.FloatField()
    max_value = models.FloatField()
    suggested_specialist = models.CharField(max_length=100)  # like 'Endocrinologist'

    def __str__(self):
        return f"{self.test_name} ➜ {self.suggested_specialist}"

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.specialty})"




from django.db import models

class Order(models.Model):
    ORDER_STATUS = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Cancelled', 'Cancelled'),
        ('Refunded', 'Refunded'),
    ]

    order_id = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    product = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='Pending')
    order_date = models.DateTimeField(auto_now_add=True)

    def is_cancellable(self):
        return self.status == 'Pending'








