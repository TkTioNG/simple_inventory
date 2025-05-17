import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from simple_inventory.inventory.tests.factories import InventoryFactory
from simple_inventory.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestInventoryListApiView(APITestCase):
    """
    Test API for inventory list.
    """

    def setUp(self):
        self.user = UserFactory()
        self.inventory = InventoryFactory()

    def test_success_view(self):
        url = reverse("api:inventory-list")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["id"] == self.inventory.id

    def test_search_name(self):
        url = reverse("api:inventory-list")
        self.client.force_authenticate(user=self.user)

        # Should return 1 result
        response = self.client.get(
            url,
            data={"name": self.inventory.name},
            format="json",
        )
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["id"] == self.inventory.id

        # Should return 0 results
        response = self.client.get(url, data={"name": "random-name"}, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 0


class TestInventoryListView(APITestCase):
    """
    Test template view for inventory list.
    """

    def setUp(self):
        self.user = UserFactory()
        self.inventory = InventoryFactory()

    def test_success_view(self):
        url = reverse("inventory:inventory-list")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK


class TestInventoryDetailView(APITestCase):
    """
    Test template view for inventory detail.
    """

    def setUp(self):
        self.user = UserFactory()
        self.inventory = InventoryFactory()

    def test_success_view(self):
        url = reverse("inventory:inventory-detail", kwargs={"pk": self.inventory.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
