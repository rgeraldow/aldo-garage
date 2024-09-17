import uuid
from django.db import models

class CarEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    car_horsepower = models.IntegerField(default=0)

