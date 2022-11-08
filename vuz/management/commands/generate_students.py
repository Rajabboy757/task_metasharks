# python manage.py generate_students.py

from django.core.management.base import BaseCommand
from vuz.models import User, Type, StudentGroup, Direction
from random import randint
import names

class Command(BaseCommand):
    help = 'generates multiple students'

    def handle(self, *args, **kwargs):
        self.stdout.write('...')
        self.stdout.write('100 random Student Generating command is started...')

        l = []

        for i in range(100):
            a = User()
            a.first_name = names.get_first_name()
            a.last_name = names.get_last_name()
            a.username = str(a.first_name) + str(a.last_name)
            a.type = Type.student
            a.ole = StudentGroup.objects.all()[randint(1, 5)]
            # a.direction_curator = Direction.objects.all()[randint(0, 4)]
            a.save()
            l.append(a)

        if len(l) >= 100:
            self.stdout.write('100 random Students has been generated Successfully !!!')
            self.stdout.write('\n')
