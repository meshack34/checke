from datetime import datetime
from django.db import models

from datetime import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import date
from datetime import datetime
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.shortcuts import redirect
from multiselectfield import MultiSelectField
from django.db import models
from django.contrib.auth.models import  AbstractBaseUser , BaseUserManager, PermissionsMixin

# Create your models here.
# models.py

from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    description2 = models.TextField(null=True)
    caption = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class AccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username = username,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    email           = models.EmailField(max_length=100, unique=True)
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    phone_number    = models.CharField(max_length=50)
    user_type    = models.CharField(max_length=50)
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active        = models.BooleanField(default=True)
    is_superadmin        = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = AccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class Patient(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    profile_image = models.ImageField(upload_to='patients/%Y/%m/%d/', default='default.png')
    city = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    blood_group = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=True)
    date_joined = models.DateTimeField(default=date.today, blank=True)
    date_of_birth = models.DateField(null=True)
    age_years = models.PositiveIntegerField(null=True)  

    @property
    def calculate_age(self):  # Rename the property
        today = date.today()
        if self.date_of_birth:
            age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
            return age
        return None
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    

class Doctor(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)  
    date_joined = models.DateTimeField(default=date.today, blank=True)
    user = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=True)
    address  = models.CharField(max_length=50)
    date_joined = models.DateTimeField(default=datetime.now, blank=True)
    profile_image = models.ImageField(upload_to='doctors/%Y/%m/%d/',default='default.png')
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    

class DoctorSpecialization(models.Model):
    doctor_category  = models.CharField(max_length=50, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.doctor_category




# for when patient select appoint time from patient dashboard
class PatientAppointment(models.Model):
    appoint_date = models.CharField(max_length=50, null=True)
    appoint_time = models.CharField(max_length=50, null=True)
    appoint_day = models.CharField(max_length=50, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True)
    month = models.CharField(max_length=50, null=True)
    date = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.patient


# for doctor only. Doc will select time slot for his/her appointment
class AppointmentTime(models.Model):
    day = models.CharField(max_length=50, null=True)
    time_from = models.CharField(max_length=50, null=True)
    time_to = models.CharField(max_length=50, null=True)
    from_to = models.CharField(max_length=50, null=True)
    appointment_date = models.DateField(null=True)
    month = models.CharField(max_length=50, null=True)
    date = models.CharField(max_length=50, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.day


    

class MedicalRecords(models.Model):
    medical_insurance =  models.FileField(upload_to='insurance/%Y/% m/% d/')
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True)
    class Meta:
        verbose_name_plural = "MedicalRecords"

    def __str__(self):
        return self.patient.user.first_name



class CurrentMedication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=100)
    reason = models.CharField(max_length=200)
    date = models.DateField()

class Allergy(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    allergy_name = models.CharField(max_length=100)
    severity = models.CharField(max_length=50)
    diagnosis_date = models.DateField()

class Surgery(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    surgery_type = models.CharField(max_length=100)
    surgery_date = models.DateField()
    reason = models.CharField(max_length=200)

class ImmunizationHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=100)
    date = models.DateField()

class FamilyMedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medical_condition = models.CharField(max_length=100)
    affected_member_name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)

class MedicalHistoryy(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    reason =  models.CharField(max_length=200, blank=True)
    ever_had = models.CharField(max_length=200,blank=True)
    
    weight = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=10, null=True)
    blood_group = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(null=True)
    age_years = models.PositiveIntegerField(null=True)
    
    other_illness = models.CharField(max_length=200,blank=True)
    other_information = models.CharField(max_length=200,blank=True)
    is_processing = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name_plural = "MedicalHistories"

   


class Prescription(models.Model):
    name =  models.CharField(max_length=50, null=True)
    quantity  = models.CharField(max_length=50, null=True)
    days = models.CharField(max_length=50, null=True)
    morning = models.CharField(max_length=10, null=True)
    afternoon = models.CharField(max_length=10, null=True)
    evening = models.CharField(max_length=10, null=True)
    night = models.CharField(max_length=10, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True)
    uploaded_date = models.DateTimeField(default=datetime.now, blank=True)
    def __int__(self):
        return self.id
   
class PrescriptionStatus(models.Model):
    is_uploaded= models.BooleanField(default=False)
    newprescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __int__(self):
        return self.id

class Treatment(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    def __str__(self):
        return f'{self.name} - {self.price}'
    
class ReviewofSystem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    def __str__(self):
        return f'{self.name} - {self.price}'
    

class Examination(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    def __str__(self):
        return f'{self.name} - {self.price}'
    
class Diagnosis(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    def __str__(self):
        return f'{self.name} - {self.price}'
    
class Investigation(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    def __str__(self):
        return f'{self.name} - {self.price}'
    
class Consultation(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    def __str__(self):
        return f'{self.name} - {self.price}'
       
class Medication(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    def __str__(self):
        return f'{self.name} - {self.price}'
    
class PaymentType(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Medical_History(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True)
    history = models.CharField(max_length=255)
    review_of_systems = models.ManyToManyField(ReviewofSystem)
    examination = models.ManyToManyField(Examination)
    diagnosis = models.ManyToManyField(Diagnosis)
    treatment = models.ManyToManyField(Treatment)
    investigation = models.ManyToManyField(Investigation)
    medication = models.ManyToManyField(Medication)
    consultation = models.ManyToManyField(Consultation)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    follow_up_date = models.DateField(null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.patient.user.first_name} - {self.patient.user.last_name}'
    def calculate_total_price(self):
    # Calculate total price based on selected categories, categories2, and categories3
        total_price = sum(category.price for category in self.review_of_systems.all())
        total_price += sum(category.price for category in self.examination.all())
        total_price += sum(category.price for category in self.diagnosis.all())
        total_price += sum(category.price for category in self.treatment.all())
        total_price += sum(category.price for category in self.investigation.all())
        total_price += sum(category.price for category in self.medication.all())
        total_price += sum(category.price for category in self.consultation.all())
        return total_price
    

    class Meta:
        verbose_name_plural = 'Medical History'


class Appointment(models.Model):
    appointment_date  = models.DateField(null=True)
    appointment_status  = models.BooleanField(default='inactive')
    booking_date  = models.DateField(null=True)
    followup_date  = models.DateField(null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.patient.user.first_name
    
    
    
 # Make sure to import Patient if it's defined in another module

# class LabData(models.Model):
#     LAB_DATA_CHOICES = [
#         ('labtest', 'Lab Test'),
#         ('labreport', 'Lab Report'),
#         ('testresult', 'Test Result'),
#     ]

#     data_type = models.CharField(max_length=10, choices=LAB_DATA_CHOICES)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     date_of_collection = models.DateTimeField()
#     ordering_physician = models.CharField(max_length=100)
#     specimen_type = models.CharField(max_length=100, blank=True, null=True)
#     comments = models.TextField(blank=True, null=True)
#     name = models.CharField(max_length=100, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     normal_range = models.CharField(max_length=50, blank=True, null=True)
#     test_code = models.CharField(max_length=20, unique=True, blank=True, null=True)
#     methodology = models.TextField(blank=True, null=True)
#     result_value = models.FloatField(blank=True, null=True)
#     units = models.CharField(max_length=20, blank=True, null=True)
#     is_abnormal = models.BooleanField(default=False)
#     reference_range = models.CharField(max_length=50, blank=True, null=True)

#     def __str__(self):
#         return f"Lab Data - Type: {self.get_data_type_display()}, Patient: {self.patient}, Date: {self.date_of_collection}"
from django.db import models
from .models import Patient, Doctor

class LabReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    test_result = models.DecimalField(max_digits=10, decimal_places=2)
    test_unit = models.CharField(max_length=20)
    normal_range_min = models.DecimalField(max_digits=10, decimal_places=2)
    normal_range_max = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    specimen_type = models.CharField(max_length=50)
    collection_date_time = models.DateTimeField()
    lab_name = models.CharField(max_length=100)
    report_number = models.CharField(max_length=20)
    report_generated_date_time = models.DateTimeField()
    signature = models.CharField(max_length=100)
    credentials = models.CharField(max_length=100)
    additional_notes = models.TextField()
    barcode = models.CharField(max_length=50)
