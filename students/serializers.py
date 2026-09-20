from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    """Serializer for Student model"""

    class Meta:
        model = Student
        fields = ['student_id', 'first_name', 'last_name', 'email', 'program', 'department','semester']
        read_only_fields = ['student_id', 'date_of_birth']


    def validate_email(self, value):
        if Student.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value