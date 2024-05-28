from django.core.management.base import BaseCommand
from accounts.models import Portfolio

class Command(BaseCommand):
    help = 'Create portfolio items'

    def handle(self, *args, **kwargs):
        portfolios = [
            {
                "title": "Cruddur",
                "description": "Developed a Twitter application using AWS as the main cloud provider.",
                "image": "static/portfolio/cruddur.webp",
                "client_testimonial": ""
            },
             {
                "title": "Terrahouses",
                "description": "Developed an application where users can upload and share websites.",
                "image": "static/portfolio/terrahouse.webp",
                "client_testimonial": ""
            },
            {
                "title": "Tausendlin",
                "description": "An imaginative journey through Tausendlin, offering vibrant and diverse experiences.",
                "image": "static/portfolio/tausendlin.webp",
                "client_testimonial": ""
            },
            {
                "title": "pokemon-memory-cards-game",
                "description": "A fun and challenging Pokémon Memory Card Game for all ages with vibrant graphics.",
                "image": "static/portfolio/pokemon.webp",
                "client_testimonial": ""
            },
            {
                "title": "Enigma",
                "description": "A thrilling game where you decode messages and solve puzzles using the Enigma machine.",
                "image": "static/portfolio/enigma_machine.webp",
                "client_testimonial": ""
            },
            {
                "title": "Consulting",
                "description": "A comprehensive consulting service tailored to meet client needs.",
                "image": "static/portfolio/enigma_machine.webp",
                "client_testimonial": ""
            },
            {
                "title": "Predictive Analytics",
                "description": "Coming soon.",
                "image": "static/portfolio/predictive_analytics.webp",
                "client_testimonial": ""
            }
        ]

        for portfolio_data in portfolios:
            portfolio, created = Portfolio.objects.get_or_create(**portfolio_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Portfolio item "{portfolio.title}" created successfully.'))
            else:
                self.stdout.write(self.style.WARNING(f'Portfolio item "{portfolio.title}" already exists.'))
