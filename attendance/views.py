from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone

from students.models import Student
from .models import Attendance


@login_required
def attendance_page(request):

    # -----------------------------
    # SAVE ATTENDANCE
    # -----------------------------
    if request.method == "POST":

        semester = request.POST.get("semester", "")
        batch = request.POST.get("batch", "")
        selected_date = request.POST.get("attendance_date", "")

        if not selected_date:
            selected_date = str(timezone.localdate())

        students = Student.objects.filter(
            status="active"
        ).order_by("student_id")

        if semester:
            students = students.filter(
                semester=semester
            )

        if batch:
            students = students.filter(
                batch=batch
            )

        for student in students:

            status = request.POST.get(
                f"status_{student.id}"
            )

            if status in ["present", "absent"]:

                Attendance.objects.update_or_create(
                    student=student,
                    date=selected_date,
                    defaults={
                        "status": status
                    }
                )

        return redirect(
            f"/attendance/?semester={semester}&batch={batch}&date={selected_date}"
        )


    # -----------------------------
    # DISPLAY ATTENDANCE
    # -----------------------------

    semester = request.GET.get("semester", "")
    batch = request.GET.get("batch", "")
    selected_date = request.GET.get("date", "")

    students = Student.objects.filter(
        status="active"
    ).order_by("student_id")

    if semester:
        students = students.filter(
            semester=semester
        )

    if batch:
        students = students.filter(
            batch=batch
        )


    # -----------------------------
    # EXISTING ATTENDANCE
    # -----------------------------

    attendance_records = {}

    if selected_date:

        records = Attendance.objects.filter(
            student__in=students,
            date=selected_date
        )

        attendance_records = {
            record.student_id: record.status
            for record in records
        }


    # Give each student their attendance status
    for student in students:

        student.attendance_status = attendance_records.get(
            student.id,
            ""
        )


    # -----------------------------
    # AVAILABLE BATCHES
    # -----------------------------

    batches = (
        Student.objects
        .exclude(batch__isnull=True)
        .exclude(batch="")
        .values_list("batch", flat=True)
        .distinct()
        .order_by("batch")
    )


    # -----------------------------
    # CONTEXT
    # -----------------------------

    context = {
        "students": students,
        "semester": semester,
        "batch": batch,
        "selected_date": selected_date,
        "attendance_records": attendance_records,
        "semesters": Student.SEMESTER_CHOICES,
        "batches": batches,
    }


    return render(
        request,
        "attendance/attendance.html",
        context
    )