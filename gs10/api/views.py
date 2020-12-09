# filtering
from django.shortcuts import render
from .models import  Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView

class StudentList(ListAPIView):
    # queryset = Student.objects.filter(passby='user1')
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get_queryset(self):
        user =self.request.user
        return Student.objects.filter(passby=user)