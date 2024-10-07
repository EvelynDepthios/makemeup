import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand = models.CharField(max_length=255)  # Remove `null=True, blank=True` to make it required
    product_name = models.CharField(max_length=100)  # Already required
    price = models.IntegerField()
    description = models.TextField()  # Remove `blank=True` to enforce it as required
    category = models.CharField(max_length=100)
    ratings = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )