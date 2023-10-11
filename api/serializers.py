from rest_framework import serializers
from patientapp.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
#Serializers of models

# class StudentAdmissionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=StudentAdmission
#         fields='_all_'
        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_type'] = user.user_type  # Replace 'user_type' with your actual user type field

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_type'] = self.user.user_type  # Replace 'user_type' with your actual user type field
        return data