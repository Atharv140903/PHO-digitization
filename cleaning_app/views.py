import uuid
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import ComplaintSerializer, CleaningSerializer, WorkerSerializer
from .models import Worker, Cleaning, Complaint

@api_view(['POST'])
def create_complaint(request):
    if request.method == 'POST':
        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_cleaning(request):
    if request.method == 'POST':
        serializer = CleaningSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_worker_by_id(request, worker_id):
    try:
        worker_id_str = str(worker_id)
        worker = Worker.objects.get(worker_id=worker_id_str)
        serializer = WorkerSerializer(worker)
        return Response(serializer.data)
    except Worker.DoesNotExist:
        return Response({'error': 'Worker not found'}, status=status.HTTP_404_NOT_FOUND)



# Frontend views
def home_view(request):
    return render(request, 'cleaning_app/home.html')

def complaint_form_view(request):
    return render(request, 'cleaning_app/complaint_form.html')

def cleaning_form_view(request, worker_id):
    return render(request, 'cleaning_app/cleaning_form.html', {'worker_id': worker_id})