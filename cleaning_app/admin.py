from django.contrib import admin
from .models import Worker, Cleaning, Complaint

admin.site.register(Worker)
admin.site.register(Cleaning)
admin.site.register(Complaint)
