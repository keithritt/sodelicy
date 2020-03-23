from django.core.management.base import BaseCommand, CommandError
from pprint import pprint
import time

class Command(BaseCommand):
  help = 'Runs the ticker'

  #def add_arguments(self, parser):
  #    parser.add_argument('poll_id', nargs='+', type=int)

  def handle(self, *args, **options):
    print('handle')

