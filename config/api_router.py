from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from simple_inventory.inventory.views import InventoryListAPIView
from simple_inventory.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)

urlpatterns = [
    path("inventory/", InventoryListAPIView.as_view(), name="inventory-list"),
]

app_name = "api"
urlpatterns = urlpatterns + router.urls
