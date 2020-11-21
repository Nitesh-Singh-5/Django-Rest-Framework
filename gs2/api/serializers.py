from rest_framework import serializers
from .models import *

# Validators 
# def 

class studentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self,validate_data):
        return Student.objects.create(**validate_data)

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()

        return instance

    # Field level validation
    def validate_roll(self,value):  
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value
    
    # Object Level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('city must be ranchi')
        return data