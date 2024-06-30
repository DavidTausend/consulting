from django.core.management.base import BaseCommand
from accounts.models import Certificate

class Command(BaseCommand):
    help = 'Create certificate items'

    def handle(self, *args, **kwargs):
        certificates = [
            {
                "title": "AWS Certified Cloud Practitioner",
                "description": "Credential validating expertise in AWS cloud services.",
                "image": "iui2ymmzic0svu2bea2i",  
                "issuing_organization": "Amazon Web Services",
                "date_issued": "2023-06-01",
                "expiry_date": "2026-06-01",
            },
            {
                "title": "AWS Cloud Project Bootcamp",
                "description": "Comprehensive training on AWS Cloud Projects.",
                "image": "xr7nizmkyhw3avodnwad",
                "issuing_organization": "Amazon Web Services",
                "date_issued": "2023-05-01",
                "expiry_date": "2026-05-01",
            },
            {
                "title": "AWS Certified Developer - Associate",
                "description": "Certification for demonstrating expertise in AWS development.",
                "image": "ccnss6gsh96sz0mxj65a",
                "issuing_organization": "Amazon Web Services",
                "date_issued": "2023-04-01",
                "expiry_date": "2026-04-01",
            },
            {
                "title": "AWS Certified Solutions Architect - Associate",
                "description": "Credential validating expertise in AWS architecture.",
                "image": "qirocncxltfcuwbcjr2z",
                "issuing_organization": "Amazon Web Services",
                "date_issued": "2023-03-01",
                "expiry_date": "2026-03-01",
            },
            {
                "title": "AWS Certified SysOps Administrator",
                "description": "Certification for expertise in AWS system operations.",
                "image": "hvclt4oiyqxlwn7tll6n",
                "issuing_organization": "Amazon Web Services",
                "date_issued": "2023-02-01",
                "expiry_date": "2026-02-01",
            },
            {
                "title": "Google Cloud Digital Leader",
                "description": "Certification for demonstrating expertise in Google Cloud Platform services.",
                "image": "xtkf98nngfua8l4i2tg8",
                "issuing_organization": "Google Cloud",
                "date_issued": "2023-01-01",
                "expiry_date": "2026-01-01",
            },
            {
                "title": "Google Professional Cloud Engineer",
                "description": "Credential validating expertise in Google Cloud engineering.",
                "image": "wym2ui2qqtlvtqzj1jp0",
                "issuing_organization": "Google Cloud",
                "date_issued": "2022-12-01",
                "expiry_date": "2025-12-01",
            },
            {
                "title": "Code Challenge Winner",
                "description": "Award for winning a prestigious coding challenge.",
                "image": "oksyco0dquswsf54dlav",
                "issuing_organization": "Code Challenge Organization",
                "date_issued": "2022-11-01",
                "expiry_date": None,
            },
            {
                "title": "Full Stack Developer Bootcamp",
                "description": "Comprehensive training on full stack development.",
                "image": "thogmdynmgrquw9n6vhi",
                "issuing_organization": "Bootcamp Organization",
                "date_issued": "2022-10-01",
                "expiry_date": None,
            },
            {
                "title": "HashiCorp Certified: Terraform Associate",
                "description": "Certification for expertise in Terraform.",
                "image": "e1b9mt7tmsp50j3ydmjm",
                "issuing_organization": "HashiCorp",
                "date_issued": "2022-09-01",
                "expiry_date": "2025-09-01",
            },
            {
                "title": "Terraform Bootcamp",
                "description": "Comprehensive training on Terraform.",
                "image": "ykaf04iw4s0l8wqyy5br",
                "issuing_organization": "Bootcamp Organization",
                "date_issued": "2022-08-01",
                "expiry_date": None,
            }
        ]

        for certificate_data in certificates:
            certificate, created = Certificate.objects.update_or_create(
                title=certificate_data['title'],
                defaults=certificate_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Certificate item "{certificate.title}" created successfully.'))
            else:
                self.stdout.write(self.style.WARNING(f'Certificate item "{certificate.title}" already exists.'))
