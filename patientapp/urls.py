from django.urls import path
from .import views
urlpatterns = [
    path('',views.home, name='home'),
    
    #Authentication
    path('register/',views.patientregister, name='register'),
    path('patient/dashboard/',views.patient_dashboard, name='patient_dashboard'),
    path('patient_appointment/<int:doctor_id>/', views.patient_appointment, name='patient_appointment'),
    path('appointments/', views.appointments, name="appointments"),
    path('profile/<int:doctor_id>/', views.profile, name='profile'),
    path('doctor_search/', views.doctor_search, name='doctor_search'),
    path('doctors/',views.doctors, name='doctors'),
    path('booking/<int:doctor_id>/', views.booking, name='booking'),
    path('history/', views.history, name='history'),
    path('doctor/register/',views.doc_register, name='doctor-register'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('doctor/dashboard/',views.doctor_dashboard, name='doctor_dashboard'),
    path('status/<int:patient_id>',views.status, name='status'),
    path('current/patient/<int:patient_id>/', views.current_patient, name="current_patient"),
    path('Prescription/<int:patient_id>/', views.getPrescriptionForDoc, name="getPrescriptionForDoc"),
    path('add/prescription/<int:patient_id>/', views.add_prescription, name='add_prescription'),
    path('submit/Prescription/<int:patient_id>/', views.submitPrescription, name="submitPrescription"),
    path('delete/Prescription/<int:pres_id>/', views.deletePrescItem, name="deletePrescItem"),
    
  
    # ... your other URL patterns ...
    # path('patient_treatment_history/<int:patient_id>/', views.patient_treatment_history, name='patient_treatment_history'),


    
    path('treatment/<int:patient_id>/', views.Medication, name='patient-medicals'),
    # path('add_treatment/<int:patient_id>/', views.add_treatment, name='add_treatment'),
     path('view_medical_history/<int:patient_id>/', views.view_medical_history, name='view_medical_history'),

    
    path('submitPrescription/<int:patient_id>/', views.submitPrescription, name="submitPrescription"),
    path('deletePrescItem/<int:pres_id>/', views.deletePrescItem, name="deletePrescItem"),
    path('doctor-profile/',views.doctor_profile, name='doctor_profile'),
    path('doctor_specialization/',views.doctor_specialization, name='doctor_specialization'),
    
    path('medical_history/', views.medical_history, name='medical_history'),
    path('schedule_timing/<int:doctor_id>/', views.schedule_timing, name='schedule_timing'),
    path('mypatients', views.mypatients, name='mypatients'),
    
    path('viewReview/', views.viewReview, name="viewReview"),
    path('viewReviewOnProfile/', views.viewReviewOnProfile, name="viewReviewOnProfile"),
    path('deleteAppointment/', views.deleteAppointment, name="deleteAppointment"),
    path('patients_profile/', views.patients_profile, name='patients_profile'),
    path('get_prescription/', views.getPrescription, name="getPrescription"),
    path('show_prescription/', views.show_prescription, name="show_prescription"),
]
