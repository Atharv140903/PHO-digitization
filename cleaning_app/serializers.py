from rest_framework import serializers
from .models import Cleaning, Complaint, Worker

class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = '__all__'  # To serialize all fields in the Worker model

class ComplaintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Complaint
        fields = '__all__'  # To serialize all fields in the Complaint model

class CleaningSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cleaning
        fields = '__all__'  # To serialize all fields in the Cleaning model