from django.db import models


class Products(models.Model):
    """
    Products model
    
    Attributes:
        name: The name of the product
        price: The price of the product
        quantity: The quantity of the product
    """
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        """
        Returns the string representation of the model
        """
        return self.name