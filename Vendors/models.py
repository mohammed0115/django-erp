from django.db import models
from Customers.models import Customer
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Vendor(Customer):
 
    

    class Meta:
        verbose_name ="Customer"
        verbose_name_plural = "Customers"

    # def get_absolute_url(self):
    #     return reverse("Vendor_detail", kwargs={"pk": self.pk})
