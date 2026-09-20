from  rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'code',
            'name',
            'department',
            'instructor',
            'credits',
            'duration',
            'semester',
            'capacity',
            'status',
            'description',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_code(self, value):
        if Course.objects.filter(code=value).exists():
            raise serializers.ValidationError("Course code already exists")
        return value