from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    note = models.TextField(default="")
    stock = models.PositiveIntegerField(default=0)
    availability = models.BooleanField(default=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Inventories"

    def __str__(self):
        return self.name
