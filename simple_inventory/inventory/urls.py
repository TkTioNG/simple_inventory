from django.urls import path

from simple_inventory.inventory.views import InventoryDetailView
from simple_inventory.inventory.views import InventoryListView

app_name = "inventory"
urlpatterns = [
    path("", view=InventoryListView.as_view(), name="inventory-list"),
    path("<int:pk>/", view=InventoryDetailView.as_view(), name="inventory-detail"),
]
