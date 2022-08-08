from django.core.management.base import BaseCommand, CommandError
from user.models import Gender


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        pass


    def handle(self, *args, **options):

        #seeder for genders
        genders = [{"name": "Male"},{"name": "Female"}]
        for gender in genders:
            Gender.objects.get_or_create(name=gender["name"])
