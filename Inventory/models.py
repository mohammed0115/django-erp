from django.db import models

# Create your models here.
from Products.models import Product
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
class Inventory(models.Model):
    name = models.CharField("Inventory Name", max_length=50)
    Product =models.ForeignKey(Product, verbose_name="product", on_delete=models.CASCADE)
    quan_in_stock = models.IntegerField("Total In")
    sales_quan    = models.IntegerField("Total out")

    

    class Meta:
        verbose_name = "Inventory"
        verbose_name_plural = "Inventorys"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Inventory_detail", kwargs={"pk": self.pk})
