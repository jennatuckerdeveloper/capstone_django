from django.contrib import admin
from .views import Item, Character, Inventory, Landmark

# Register your models here.
admin.site.register(Item)
admin.site.register(Character)
admin.site.register(Inventory)
admin.site.register(Landmark)
