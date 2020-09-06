from django.db import models
from Customers.models import Customer
# Create your models here.
class Vendor(Customer):
 
    

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Vendor_detail", kwargs={"pk": self.pk})
