from rest_framework import serializers
from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'department',
            'position',
            'qualification',
            'experience',
            'joining_date',
            'status',
            'bio',
        ]
        read_only_fields=['date_of_birth']
        
    def validate_email(self, value):
        if Teacher.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value