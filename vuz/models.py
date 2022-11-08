from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from rest_framework.validators import ValidationError


class Base(models.Model):
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)


class Direction(Base):
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Direction"
        verbose_name_plural = "Directions"

    def __str__(self):
        return self.name


class Type(models.Choices):
    admin = "Admin"
    student = "Student"
    Curator = "Curator"


class User(AbstractUser):
    type = models.CharField(verbose_name='Type', choices=Type.choices, max_length=255)
    ole = models.ForeignKey("StudentGroup", related_name='students',
                            on_delete=models.SET_NULL,
                            null=True)
    direction_curator = models.OneToOneField(
        Direction, related_name="curator",
        on_delete=models.SET_NULL,
        null=True
    )

    def add_user(self, student_group):
        if student_group.student_count < 20:
            self.user_group = student_group
            student_group.student_count += 1
        else:
            raise ValidationError({"detail": "Group is full"})

    def __str__(self):
        return f'{self.username}, {self.type}, {self.ole}'


class Subject(Base):
    name = models.CharField(max_length=100)
    direction_subject = models.ManyToManyField(Direction, related_name="subjects")

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.name


class StudentGroup(Base):
    name = models.CharField(max_length=50)
    student_count = models.IntegerField(default=0, validators=[MaxValueValidator(20), MinValueValidator(0)])
    group_direction = models.ForeignKey(Direction, related_name="student_group", on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "StudentGroup"
        verbose_name_plural = "StudentGroup"

    def __str__(self):
        return self.name
