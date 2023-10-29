from django.urls import path
from . import views

urlpatterns = [

    # Frontend URLs
    path('', views.home_view, name='home'),
    path('complaint/', views.complaint_form_view, name='complaint_form'),
    path('cleaning/<uuid:worker_id>/', views.cleaning_form_view, name='cleaning_form'),

    # API Endpoints
    path('api/complaint/', views.create_complaint, name='create_complaint'),
    path('api/cleaning/', views.create_cleaning, name='create_cleaning'),
    path('api/worker/<uuid:worker_id>/', views.get_worker_by_id, name='get_worker_by_id')
]