from django.contrib import admin
from .models import StudentProfile, TutorProfile, TeacherProfile, ParentProfile

# Register your models here.
admin.site.register(StudentProfile)
admin.site.register(TutorProfile)
admin.site.register(TeacherProfile)
admin.site.register(ParentProfile)
