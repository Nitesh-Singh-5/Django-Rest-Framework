# filtering generic filters

from django.shortcuts import render
from .models import  Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter

# for simple filtering

# class StudentList(ListAPIView):
    # queryset = Student.objects.filter(passby='user1')
    # queryset = Student.objects.all()
    # serializer_class = StudentSerializer
    # def get_queryset(self):
    #     user =self.request.user
    #     return Student.objects.filter(passby=user)


# generic filter

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     # filter_backend = [DjangoFilterBackend] for per view filtering
#     filterset_fields = ['city','id']


# Search Filtering

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     filter_backends = [SearchFilter]
#     # search_fields = ['city']
#     search_fields = ['name','city']

# ordering

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    

