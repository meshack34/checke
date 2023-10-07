from .models import *
from django.forms import DateInput
from django.forms.fields import DateField
from django.forms.widgets import PasswordInput
from django import forms
from django.forms import DateInput, DateField, PasswordInput

      
            
class MedicalTreatmentForm(forms.ModelForm):
    treatment = forms.ModelMultipleChoiceField(queryset=Treatment.objects.all(), widget=forms.CheckboxSelectMultiple)
    review_of_systems = forms.ModelMultipleChoiceField(queryset=ReviewofSystem.objects.all(), widget=forms.CheckboxSelectMultiple)
    examination = forms.ModelMultipleChoiceField(queryset=Examination.objects.all(), widget=forms.CheckboxSelectMultiple)
    diagnosis = forms.ModelMultipleChoiceField(queryset=Diagnosis.objects.all(), widget=forms.CheckboxSelectMultiple)
    investigation = forms.ModelMultipleChoiceField(queryset=Investigation.objects.all(), widget=forms.CheckboxSelectMultiple)
    medication = forms.ModelMultipleChoiceField(queryset=Medication.objects.all(), widget=forms.CheckboxSelectMultiple)
    consultation = forms.ModelMultipleChoiceField(queryset=Consultation.objects.all(), widget=forms.CheckboxSelectMultiple)
    follow_up_date = DateField(widget=DateInput)
    class Meta:
        model = Medical_History
        fields = ('__all__')

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput(attrs={
        
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password', 'user_type']
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
    



class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['profile_image', 'city', 'address', 'country', 'date_of_birth', 'blood_group', 'gender']

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['profile_image'].widget.attrs['class'] = 'upload'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['country'].widget.attrs['class'] = 'form-control'
        self.fields['date_of_birth'].widget.attrs['class'] = 'form-control'

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['address', 'profile_image', 'gender', 'description']

class DoctorSpecilizationForm(forms.ModelForm):
    class Meta:
        model = DoctorSpecialization
        fields = ['doctor_category',]

    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        self.fields['profile_image'].widget.attrs['class'] = 'upload'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['gender'].widget.attrs['class'] = 'form-control select'
        self.fields['description'].widget.attrs['class'] = 'form-control'



class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistoryy
        fields = [
            'reason',
            'weight',
            'other_illness',
            'other_information',
        ]

    def __init__(self, *args, **kwargs):
        super(MedicalHistoryForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


from django import forms

class FamilyMedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = FamilyMedicalHistory
        fields = [
            'medical_condition',
            'affected_member_name',
            'relationship',
        ]

    def __init__(self, *args, **kwargs):
        super(FamilyMedicalHistoryForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
from django import forms
from .models import CurrentMedication

class CurrentMedicationForm(forms.ModelForm):
    class Meta:
        model = CurrentMedication
        fields = [
            'medicine_name',
            'reason',
            'date',
        ]

    def __init__(self, *args, **kwargs):
        super(CurrentMedicationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
from django import forms
from .models import Allergy

class AllergyForm(forms.ModelForm):
    class Meta:
        model = Allergy
        fields = [
            'allergy_name',
            'severity',
            'diagnosis_date',
        ]

    def __init__(self, *args, **kwargs):
        super(AllergyForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
from django import forms
from .models import Surgery

class SurgeryForm(forms.ModelForm):
    class Meta:
        model = Surgery
        fields = [
            'surgery_type',
            'surgery_date',
            'reason',
        ]

    def __init__(self, *args, **kwargs):
        super(SurgeryForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
from django import forms
from .models import ImmunizationHistory

class ImmunizationHistoryForm(forms.ModelForm):
    class Meta:
        model = ImmunizationHistory
        fields = [
            'vaccine_name',
            'date',
        ]

    def __init__(self, *args, **kwargs):
        super(ImmunizationHistoryForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class FamilyMedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = FamilyMedicalHistory
        fields = [
            'medical_condition',
            'affected_member_name',
            'relationship',
        ]

    def __init__(self, *args, **kwargs):
        super(FamilyMedicalHistoryForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
from django import forms
from .models import LabReport

class LabReportForm(forms.ModelForm):
    class Meta:
        model = LabReport
        exclude = ['patient', 'doctor']  # Exclude patient and doctor fields from the form

