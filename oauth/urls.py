from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.oauth, name='oauth'),
    path('callback/', views.login_client, name='login_client'),
    path('logout/', views.logout_client, name='logout_client'),

]