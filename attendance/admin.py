from django.contrib import admin
from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status')
    list_filter = ('date', 'status')
    search_fields = (
        'student__student_id',
        'student__first_name',
        'student__last_name',
    )