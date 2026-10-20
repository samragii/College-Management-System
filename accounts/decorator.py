from django.contrib.auth.decorators import user_passes_test


def is_teacher(user):
    return (
        user.is_authenticated
        and user.groups.filter(name="Teacher").exists()
    )


def is_course_manager(user):
    return (
        user.is_authenticated
        and (
            user.is_superuser
            or user.groups.filter(name="Teacher").exists()
        )
    )


teacher_required = user_passes_test(is_teacher)
course_manager_required = user_passes_test(is_course_manager)
