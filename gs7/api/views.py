# JSON web token

from django.shortcuts import render
from .models import  Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes=[JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    


# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA2MjMzMjc0LCJqdGkiOiJkZjNkODUyZmFjYWQ0Y2E2OTk1NjkxMDU1ZTNlYWQwNSIsInVzZXJfaWQiOjF9.3K7BaGiKMOsGBnSKZ4OjBfz7q5rCpVu57qt5039p6yU
# http POST http://127.0.0.1:8000/verifytoken/ token="J0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA2MjMzMDYwLCJqdGkiOiJlMzJjY2Q5NmRmNzA0ZDE1OTMzZDg1NDY5NjkyOTMzNyIsInVzZXJfaWQiOjF9.wRFcPnreHrdHrMFMxN8Dw1g3B4tzT5yqypMkDcqbLFg"
# http://127.0.0.1:8000/verifytoken/ refresh="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA2MjMzMjc0LCJqdGkiOiJkZjNkODUyZmFjYWQ0Y2E2OTk1NjkxMDU1ZTNlYWQwNSIsInVzZXJfaWQiOjF9.3K7BaGiKMOsGBnSKZ4OjBfz7q5rCpVu57qt5039p6yU"