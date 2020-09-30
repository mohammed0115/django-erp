from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("category name", max_length=50,null=True)

    

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})

# Create your models here.
class Product(models.Model):
    name = models.CharField("Product Name", max_length=50)
    p_type = models.CharField("Product Type", max_length=50)
    sale_price = models.IntegerField("Sale price")
    p_cost     = models.IntegerField("Product cost")
    serial_number = models.CharField("serial number", max_length=50)
    company       = models.CharField("company production", max_length=50)
    product_created = models.DateField("date create", auto_now=False, auto_now_add=False)
    product_end     = models.DateField("End date", auto_now=False, auto_now_add=False)
    # category        = models.ForeignKey("Category", verbose_name="Category type", on_delete=models.CASCADE,null=True)
    class Meta:
        verbose_name = "Product"
        verbose_name_plural ="products"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})

