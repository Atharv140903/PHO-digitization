from django.db import models
import uuid 

class Worker (models.Model):
        worker_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
        worker_name = models.CharField(max_length=100)

        def __str__(self):
            return f'{self.worker_name} - {self.worker_id}'
        
class Cleaning (models.Model):
        task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
        worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
        roll_number = models.CharField(max_length=10)
        name_of_student = models.CharField(max_length=100)
        hostel = models.CharField(max_length=50)
        room_number = models.CharField(max_length=10)
        wing = models.CharField(max_length=10)
        task_choices = [
            ('room', 'Room'),
            ('washroom', 'Washroom'),
            ('corridor', 'Corridor'),
            ]
        cleaning_task = models.CharField(max_length=10, choices=task_choices)
        task_description = models.TextField(max_length=255, default='No description provided')
        date_time = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f'{self.hostel} - {self.room_number} - {self.date_time}'
        
class Complaint (models.Model):
        complaint_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
        roll_number = models.CharField(max_length=10)
        name_of_student = models.CharField(max_length=100)
        complaint = models.TextField()
        date_time = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f'{self.name_of_student} - {self.date_time}'