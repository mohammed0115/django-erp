from django.db import models
from Customers.models import Customer
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Vendor(Customer):
    
    

    class Meta:
        verbose_name ="Vendor"
        verbose_name_plural = "Vendor"

    def get_absolute_url(self):
        return reverse("Vendor_detail", kwargs={"pk": self.pk})
