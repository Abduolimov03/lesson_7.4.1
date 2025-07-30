from django.db import models

class Watch(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __int__(self):
        return self.brand
