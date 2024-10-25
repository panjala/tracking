from django.shortcuts import render

# Create your views here.
# tracking/views.py
import hashlib
import uuid
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class GenerateTrackingNumberAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # Extract query parameters
            origin_country_id = request.query_params.get('origin_country_id')
            destination_country_id = request.query_params.get('destination_country_id')
            weight = request.query_params.get('weight')
            created_at = request.query_params.get('created_at')
            customer_id = request.query_params.get('customer_id')
            customer_name = request.query_params.get('customer_name')
            customer_slug = request.query_params.get('customer_slug')

            # Ensure all required parameters are provided
            if not all([origin_country_id, destination_country_id, weight, created_at, customer_id, customer_name, customer_slug]):
                return Response({"error": "Missing required query parameters"}, status=status.HTTP_400_BAD_REQUEST)

            # Use customer_id, created_at, and other values to create a unique tracking number
            base_string = f"{origin_country_id}{destination_country_id}{weight}{created_at}{customer_id}{customer_name}"

            # Hash the base string to create a unique identifier
            tracking_hash = hashlib.sha256(base_string.encode()).hexdigest()[:16].upper()

            # Ensure tracking number matches the regex pattern
            tracking_number = ''.join(filter(str.isalnum, tracking_hash))[:16]  # Limit to 16 characters, alphanumeric

            # Get the current timestamp in RFC 3339 format
            created_timestamp = datetime.now().isoformat()

            # Return the tracking number and creation timestamp
            return Response({
                "tracking_number": tracking_number,
                "created_at": created_timestamp
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
