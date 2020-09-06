from django.db import models

# Create your models here.
class Customer(models.Model):
    fname   = models.CharField("First name", max_length=50)
    minName = models.CharField("Miduim name", max_length=50)
    lname   = models.CharField("Last name", max_length=50)
    email   = models.EmailField("Email", max_length=254)
    phone   = models.CharField("phone number", max_length=50)
    nationalno = models.CharField("national number", max_length=50)

    

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Customer_detail", kwargs={"pk": self.pk})
