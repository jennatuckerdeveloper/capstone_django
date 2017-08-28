import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'capstone.settings')
import django

django.setup()

from game.models import Item, Inventory, Character, Landmark, Game
from authentication.models import User

