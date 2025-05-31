from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with listings'

    def handle(self, *args, **kwargs):
        sample_data = [
            {"title": "Cozy Cottage", "description": "A cozy cottage in the woods", "location": "Nairobi", "price_per_night": 45.00},
            {"title": "Beach Bungalow", "description": "A peaceful house by the sea", "location": "Mombasa", "price_per_night": 90.00},
            {"title": "Mountain Cabin", "description": "Scenic mountain views", "location": "Mount Kenya", "price_per_night": 70.00}
        ]

        for data in sample_data:
            Listing.objects.create(**data)

        self.stdout.write(self.style.SUCCESS("Database seeded with sample listings!"))
