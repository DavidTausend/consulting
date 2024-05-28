from django.core.management.base import BaseCommand
from accounts.models import Portfolio

class Command(BaseCommand):
    help = 'Create portfolio items'

    def handle(self, *args, **kwargs):
        portfolios = [
            {
                "title": "aws-bootcamp-cruddur-2023",
                "description": "Developed an twitter application with only cloud compones and using aws as main cloud provide.",
                "image": "",
            }
        ]

        for portfolio_data in portfolios:
            portfolio, created = Portfolio.objects.get_or_create(**portfolio_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Portfolio item "{portfolio.title}" created successfully.'))
            else:
                self.stdout.write(self.style.WARNING(f'Portfolio item "{portfolio.title}" already exists.'))
