from django.urls import path, include
from .views import PatientAPIView, PatientDetailAPIView

urlpatters = [
    path('patient/', PatientAPIView.as_view(), name="pacientes"),
    path('patient2/<pk>/', PatientDetailAPIView.as_view(), name="especifico")
    ] 
