from django.db import models

from users.models import User
from products.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE) #Uno a muchos
    products = models.ManyToManyField(Product) #Muchos a muchos
    subtotal = models.DecimalField(default=0.0, max_digits=8,decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8,decimal_places=2)
    creates_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ''
