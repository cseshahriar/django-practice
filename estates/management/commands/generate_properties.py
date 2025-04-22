from django.core.management.base import BaseCommand
from estates.models import Location, Property
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Generates 100,000 fake property records'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # First create some locations (100 cities)
        self.stdout.write("Creating locations...")
        locations = []
        for _ in range(100):
            loc = Location(
                city=fake.city(),
                state=fake.state(),
                country=fake.country_code(),
                zip_code=fake.zipcode()
            )
            loc.save()
            locations.append(loc)

        # Property types with weights (some types more common than others)
        property_types = [
            ('HOUSE', 0.4),
            ('APARTMENT', 0.3),
            ('CONDO', 0.15),
            ('TOWNHOUSE', 0.1),
            ('LAND', 0.05)
        ]

        # Generate 100,000 properties in batches
        batch_size = 1000
        total_properties = 100000
        self.stdout.write(f"Creating {total_properties} properties...")

        for i in range(0, total_properties, batch_size):
            batch = []
            for _ in range(batch_size):
                # Weighted random choice for property type
                prop_type = random.choices(
                    [pt[0] for pt in property_types],
                    weights=[pt[1] for pt in property_types]
                )[0]

                # Generate property data
                prop = Property(
                    name=f"{fake.word().capitalize()} {random.choice(['Residence', 'Home', 'Villa', 'Place', 'House', 'Apartment'])}",
                    description=fake.paragraph(nb_sentences=5),
                    property_type=prop_type,
                    location=random.choice(locations),
                    square_feet=random.randint(500, 5000) if prop_type != 'LAND' else random.randint(1000, 1000000),
                    bedrooms=random.randint(1, 5) if prop_type != 'LAND' else 0,
                    bathrooms=random.randint(1, 4) if prop_type != 'LAND' else 0,
                    has_garage=random.choice([True, False]),
                    has_balcony=random.choice([True, False]) if prop_type in ['APARTMENT', 'CONDO'] else False
                )
                batch.append(prop)

            # Bulk create for performance
            Property.objects.bulk_create(batch)

            # Progress update
            created = min(i + batch_size, total_properties)
            self.stdout.write(
                f"Created {created}/{total_properties} properties...")

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {total_properties} properties!")
        )
