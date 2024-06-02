from django.core.management.base import BaseCommand
from accounts.models import Certificate

class Command(BaseCommand):
    help = 'Create certificate items'

    def handle(self, *args, **kwargs):
        certificates = [
            {
                "title": "AWS Certified Cloud Practitioner",
                "description": "Amazon Web Services (AWS) - Issued Mar 2023 - Expires Mar 2026",
                "image": "images/certificates/aws_cloud_practitioner.webp"
            },
            {
                "title": "AWS Certified Solutions Architect – Associate",
                "description": "Amazon Web Services (AWS) - Issued Jun 2023 - Expires Jun 2026",
                "image": "images/certificates/aws_solutions_architect_associate.webp"
            },
            {
                "title": "AWS Certified Developer – Associate",
                "description": "Amazon Web Services (AWS) - Issued Jul 2023 - Expires Jul 2026",
                "image": "images/certificates/aws_developer_associate.webp"
            },
            {
                "title": "AWS Certified SysOps Administrator – Associate",
                "description": "Amazon Web Services (AWS) - Issued Aug 2023 - Expires Aug 2026",
                "image": "images/certificates/aws_sysops_administrator.webp"
            },
            {
                "title": "AWS Cloud Project Bootcamp Certificate (Gold Squad)",
                "description": "Credential ID iEM3yK4sJYqg7g_WCBjoew11572 - Issued Aug 2023 - Expires Aug 2026",
                "image": "images/certificates/aws_cloud_project_bootcamp.webp"
            },
            {
                "title": "HashiCorp Certified: Terraform Associate (003)",
                "description": "Issued Oct 2023 - Expires Oct 2025",
                "image": "images/certificates/terraform_associate.webp"
            },
            {
                "title": "Terraform Beginner Bootcamp (Terraformer)",
                "description": "Credential ID Pmi6FzvAMpCy60qtyomtkg11572 - Issued Oct 2023",
                "image": "images/certificates/terraform_bootcamp.webp"
            },
            {
                "title": "Code Challenge",
                "description": "Code Institute Code Cahllenge",
                "image": "images/certificates/full_stack_developer.webp"
            },
            {
                "title": "Full Stack Developer",
                "description": "Coming soon - Full Stack Developer Certificate",
                "image": "images/certificates/full_stack_developer.webp"
            },
            {
                "title": "Cloud Digital Leader",
                "description": "Coming soon - Cloud Digital Leader Certificate",
                "image": "images/certificates/cloud_digital_leader.webp",
            },
            {
                "title": "Cloud Engineer",
                "description": "Coming soon - Cloud Engineer Certificate",
                "image": "images/certificates/cloud_engineer.webp",
            }
        ]

        for certificate_data in certificates:
            certificate, created = Certificate.objects.get_or_create(**certificate_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Certificate "{certificate["title"]}" created successfully.'))
            else:
                self.stdout.write(self.style.WARNING(f'Certificate "{certificate["title"]}" already exists.'))
