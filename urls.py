# tracking/urls.py
from django.urls import path
from .views import GenerateTrackingNumberAPIView

urlpatterns = [
    path('next-tracking-number/', GenerateTrackingNumberAPIView.as_view(), name='next-tracking-number'),
]
