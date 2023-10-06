from django.contrib import admin

from .models import *
from django.contrib import admin
from .models import Doctor, DoctorSpecialization, AppointmentTime,PatientAppointment



admin.site.register(Patient)
admin.site.register(Card)

admin.site.register(PrescriptionStatus)

admin.site.register(Doctor)
admin.site.register(DoctorSpecialization)
admin.site.register(AppointmentTime)
admin.site.register(PatientAppointment)


class MedicalHistoryAdmin(admin.ModelAdmin):

    list_display = ('patient','doctor', 'is_active', 'date_created')
    list_display_links = ('patient', 'doctor')

class PrescriptionAdmin(admin.ModelAdmin):

    list_display = ('name','quantity', 'days', 'doctor', 'patient')
    list_display_links = ('name', 'patient', 'doctor')

admin.site.register(MedicalHistoryy,MedicalHistoryAdmin)
admin.site.register(MedicalRecords)
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(Medical_History)
admin.site.register(Treatment)
admin.site.register(ReviewofSystem)
admin.site.register(Examination)
admin.site.register(Consultation)
admin.site.register(Diagnosis)
admin.site.register(Investigation)
admin.site.register(Medication)
admin.site.register(PaymentType)

