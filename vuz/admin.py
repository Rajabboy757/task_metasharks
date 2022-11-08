from django.contrib import admin
from vuz.models import *


@admin.register(User)
class DevAdmin(admin.ModelAdmin):
    pass


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    pass


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    pass
