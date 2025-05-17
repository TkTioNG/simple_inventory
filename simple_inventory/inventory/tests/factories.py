from factory import SubFactory
from factory.django import DjangoModelFactory

from simple_inventory.inventory.models import Inventory
from simple_inventory.inventory.models import Supplier


class SupplierFactory(DjangoModelFactory[Supplier]):
    class Meta:
        model = Supplier


class InventoryFactory(DjangoModelFactory[Inventory]):
    supplier = SubFactory(SupplierFactory)

    class Meta:
        model = Inventory
