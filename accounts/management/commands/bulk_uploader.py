import os
import cloudinary.uploader
from django.core.management.base import BaseCommand
from accounts.models import Portfolio, Certificate


class Command(BaseCommand):
    help = 'Upload images to Cloudinary and save their details in the db.'

    def handle(self, *args, **kwargs):
        def upload_images_to_folder(folder, model, field_name, extra_fields={}):
            if os.path.exists(folder):
                for filename in os.listdir(folder):
                    if filename.endswith(('.webp')):
                        file_path = os.path.join(folder, filename)
                        response = cloudinary.uploader.upload(file_path)
                        print(f"Uploaded {filename}")
                        print(f"URL: {response['url']}")
                        print(f"Public ID: {response['public_id']}")

                        # Create or update the database record
                        defaults = {field_name: response['public_id']}
                        defaults.update(extra_fields)
                        model.objects.update_or_create(
                            title=filename.split('.')[0], defaults=defaults
                        )
            else:
                print(f"Directory {folder} does not exist.")

        # Define the folders to upload
        folders_to_upload = [
            {
                'folder': os.path.join(
                    os.path.dirname(__file__),
                    '../../../static/images/portfolio'
                ),
                'model': Portfolio,
                'field_name': 'image'
            },
            {
                'folder': os.path.join(
                    os.path.dirname(__file__),
                    '../../../static/images/certificates'
                ),
                'model': Certificate,
                'field_name': 'image',
                'extra_fields': {
                    'date_of_issuance': '2023-01-01'
                }
            },  # Example date
        ]

        for folder_info in folders_to_upload:
            print(f"Processing folder: {folder_info['folder']}")
            upload_images_from_folder(
                folder_info['folder'],
                folder_info['model'],
                folder_info['field_name'],
                folder_info.get('extra_fields', {})
            )
