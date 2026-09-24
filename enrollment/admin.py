from django.contrib import admin
from .models import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "course",
        "enrolled_date",
    )

    list_filter = (
        "course",
        "enrolled_date",
    )

    search_fields = (
        "student__student_id",
        "student__first_name",
        "student__last_name",
        "course__code",
        "course__name",
    )