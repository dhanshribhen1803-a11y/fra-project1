from django.db import models

class Claim(models.Model):
    name = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    land_area = models.CharField(max_length=50)
    land_type = models.CharField(max_length=50)

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
        ("Forwarded", "Forwarded"),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    def __str__(self):
        return self.name
