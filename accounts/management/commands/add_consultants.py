from django.core.management.base import BaseCommand
from accounts.models import Consultant


class Command(BaseCommand):
    help = 'Add consultant entries to the database'

    def handle(self, *args, **kwargs):
        consultants = [
            {
                'name': 'David Tausend',
                'title': 'Junior Cloud Consulting',
                'bio': (
                    'David is a recent graduate with a fresh perspective on '
                    'Full Stack practices.'
                ),
                'specialties': 'AWS, Full Stack, Containers',
            },
        ]

        for consultant_data in consultants:
            consultant, created = Consultant.objects.get_or_create(
                name=consultant_data['name'],
                defaults={
                    'title': consultant_data['title'],
                    'bio': consultant_data['bio'],
                    'specialties': consultant_data['specialties'],
                }
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully added consultant: {consultant.name}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Consultant already exists: {consultant.name}"
                    )
                )
