import django_filters.rest_framework
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from simple_inventory.inventory.models import Inventory
from simple_inventory.inventory.serializers import InventorySerializer


class InventoryListFilterView(ListAPIView):
    """
    Base API view for inventory list.
    """

    serializer_class = InventorySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ("name",)

    def get_queryset(self):
        return Inventory.objects.select_related("supplier").all()


class InventoryListAPIView(InventoryListFilterView):
    """
    API for inventory list.
    """


class InventoryListView(InventoryListFilterView):
    """
    Template view for inventory list.
    """

    renderer_classes = [TemplateHTMLRenderer]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {"inventories": serializer.data},
            template_name="inventory/inventory_list.html",
        )


class InventoryDetailView(RetrieveAPIView):
    """
    Template view for inventory detail.
    """

    queryset = Inventory.objects.all()
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response(
            {"inventory": self.object},
            template_name="inventory/inventory_detail.html",
        )
