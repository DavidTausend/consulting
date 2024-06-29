from django.core.management.base import BaseCommand
from accounts.models import Portfolio

class Command(BaseCommand):
    help = 'Create portfolio items'

    def handle(self, *args, **kwargs):
        portfolios = [
            {
                "title": "Cruddur",
                "description": "Developed a Twitter application using AWS as the main cloud provider.",
                "image": "gpuw53r3dimcrn6ztkww",  
                "client_testimonial": "This project significantly improved our operational efficiency and scalability."
            },
            {
                "title": "Terrahouses",
                "description": "Developed an application where users can upload and share websites.",
                "image": "rllmbyb5dxlctzwkskqr", 
                "client_testimonial": "The platform has been a game-changer for our content-sharing needs."
            },
            {
                "title": "Tausendlin",
                "description": "An imaginative journey through Tausendlin, offering vibrant and diverse experiences.",
                "image": "oog7prgtjdkrgeophytz",  
                "client_testimonial": "A unique and engaging platform that showcases the best of our city."
            },
            {
                "title": "Pokemon Memory Cards Game",
                "description": "A fun and challenging Pokémon Memory Card Game for all ages with vibrant graphics.",
                "image": "t7dl3gc13j2jpwga2fwc",  
                "client_testimonial": "An exciting game that keeps both kids and adults entertained for hours."
            },
            {
                "title": "Enigma",
                "description": "A thrilling game where you decode messages and solve puzzles using the Enigma machine.",
                "image": "hkveted51os5rqxhbiyn",
                "client_testimonial": "A captivating blend of logic, deduction, and historical intrigue."
            },
            {
                "title": "Consulting",
                "description": "A comprehensive consulting service tailored to meet client needs.",
                "image": "wolgipemdvxubxucdtpx",  
                "client_testimonial": "Exceptional consulting services that provided great insights and solutions."
            },
            {
                "title": "Predictive Analytics",
                "description": "Coming soon.",
                "image": "fk4al7lindm6xxrnvndz", 
                "client_testimonial": ""
            }
        ]

        for portfolio_data in portfolios:
            portfolio, created = Portfolio.objects.update_or_create(
                title=portfolio_data['title'],
                defaults=portfolio_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Portfolio item "{portfolio.title}" created successfully.'))
            else:
                self.stdout.write(self.style.WARNING(f'Portfolio item "{portfolio.title}" already exists.'))
