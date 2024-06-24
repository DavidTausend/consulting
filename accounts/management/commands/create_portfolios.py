from django.core.management.base import BaseCommand
from accounts.models import Portfolio
import os

class Command(BaseCommand):
    help = 'Create portfolio items'

    def handle(self, *args, **kwargs):
        portfolios = [
            {
                "title": "Cruddur",
                "description": "Developed a Twitter application using AWS as the main cloud provider.",
                "image": "images/portfolio/cruddur.webp",
                "client_testimonial": "This project significantly improved our operational efficiency and scalability."
            },
            {
                "title": "Terrahouses",
                "description": "Developed an application where users can upload and share websites.",
                "image": "images/portfolio/terrahouse.webp",
                "client_testimonial": "The platform has been a game-changer for our content-sharing needs."
            },
            {
                "title": "Tausendlin",
                "description": "An imaginative journey through Tausendlin, offering vibrant and diverse experiences.",
                "image": "images/portfolio/tausendlin.webp",
                "client_testimonial": "A unique and engaging platform that showcases the best of our city."
            },
            {
                "title": "Pokemon Memory Cards Game",
                "description": "A fun and challenging Pokémon Memory Card Game for all ages with vibrant graphics.",
                "image": "images/portfolio/pokemon.webp",
                "client_testimonial": "An exciting game that keeps both kids and adults entertained for hours."
            },
            {
                "title": "Enigma",
                "description": "A thrilling game where you decode messages and solve puzzles using the Enigma machine.",
                "image": "images/portfolio/enigma_machine.webp",
                "client_testimonial": "A captivating blend of logic, deduction, and historical intrigue."
            },
            {
                "title": "Consulting",
                "description": "A comprehensive consulting service tailored to meet client needs.",
                "image": "images/portfolio/consulting.webp",
                "client_testimonial": "Exceptional consulting services that provided great insights and solutions."
            },
            {
                "title": "Predictive Analytics",
                "description": "Coming soon.",
                "image": "images/portfolio/predictive_analytics.webp",
                "client_testimonial": ""
            }
        ]

        for portfolio_data in portfolios:
            portfolio, created = Portfolio.objects.get_or_create(**portfolio_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Portfolio item "{portfolio.title}" created successfully.'))
            else:
                self.stdout.write(self.style.WARNING(f'Portfolio item "{portfolio.title}" already exists.'))
