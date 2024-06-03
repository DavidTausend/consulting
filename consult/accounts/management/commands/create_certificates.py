from django.core.management.base import BaseCommand
from accounts.models import Certificate
from datetime import date

class Command(BaseCommand):
    help = 'Create certificate items'

    def handle(self, *args, **kwargs):
        certificates = [
            {
                "title": "AWS Certified Cloud Practitioner",
                "description": "Amazon Web Services (AWS)",
                "image": "images/certificates/aws_cloud_practitioner.webp",
                "date_of_issuance": date(2023, 3, 1)
            },
            {
                "title": "AWS Certified Solutions Architect – Associate",
                "description": "Amazon Web Services (AWS)",
                "image": "images/certificates/aws_solutions_architect_associate.webp",
                "date_of_issuance": date(2023, 6, 1)
            },
            {
                "title": "AWS Certified Developer – Associate",
                "description": "Amazon Web Services (AWS)",
                "image": "images/certificates/aws_developer_associate.webp",
                "date_of_issuance": date(2023, 7, 1)
            },
            {
                "title": "AWS Certified SysOps Administrator – Associate",
                "description": "Amazon Web Services (AWS)",
                "image": "images/certificates/aws_sysops_administrator.webp",
                "date_of_issuance": date(2023, 8, 1)
            },
            {
                "title": "AWS Cloud Project Bootcamp Certificate (Gold Squad)",
                "description": "ExamPro",
                "image": "images/certificates/aws_cloud_project_bootcamp.webp",
                "date_of_issuance": date(2023, 8, 1)
            },
            {
                "title": "HashiCorp Certified: Terraform Associate (003)",
                "description": "HashiCorp",
                "image": "images/certificates/terraform_associate.webp",
                "date_of_issuance": date(2023, 10, 1)
            },
            {
                "title": "Terraform Beginner Bootcamp (Terraformer)",
                "description": "ExamPro",
                "image": "images/certificates/terraform_bootcamp.webp",
                "date_of_issuance": date(2023, 10, 1)
            },
            {
                "title": "Code Challenge",
                "description": "Code Institute Code Challenge",
                "image": "images/certificates/code_challenge.webp",
                "date_of_issuance": date.today()
            },
            {
                "title": "Full Stack Developer",
                "description": "Coming soon - Full Stack Developer Certificate",
                "image": "images/certificates/full_stack_developer.webp",
                "date_of_issuance": date.today()
            },
            {
                "title": "Cloud Digital Leader",
                "description": "Coming soon - Cloud Digital Leader Certificate",
                "image": "images/certificates/cloud_digital_leader.webp",
                "date_of_issuance": date.today()
            },
            {
                "title": "Cloud Engineer",
                "description": "Coming soon - Cloud Engineer Certificate",
                "image": "images/certificates/cloud_engineer.webp",
                "date_of_issuance": date.today()
            }
        ]

        for certificate_data in certificates:
            certificate, created = Certificate.objects.get_or_create(**certificate_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Certificate "{certificate_data["title"]}" created successfully.'))
            else:
                self.stdout.write(self.style.WARNING(f'Certificate "{certificate_data["title"]}" already exists.'))
