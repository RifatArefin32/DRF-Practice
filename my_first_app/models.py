from django.db import models

# Create your models here.
class Product(models.Model):
    product_code = models.BigIntegerField()
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=200)
    exp_date = models.DateField()

    def __str__(self):
        return self.name