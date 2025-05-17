from django.contrib import admin

from simple_inventory.inventory.models import Inventory
from simple_inventory.inventory.models import Supplier

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Inventory)
