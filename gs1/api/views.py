from django.shortcuts import render
from .models import Student
from .serializers import studentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def student_detail(request):
    stu = Student.objects.all()
   # print(stu)
    serializer = studentSerializer(stu,many=True)
   # print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
   # print(json_data)
    return HttpResponse(json_data,content_type = 'application/json')