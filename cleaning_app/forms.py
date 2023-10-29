from django import forms
from .models import Complaint, Cleaning

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['roll_number', 'name_of_student', 'complaint']

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Cleaning
        fields = ['roll_number', 'name_of_student', 'hostel', 'room_number', 'task_choices', 'cleaning_task', 'task_description']