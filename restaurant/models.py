from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(no_of_guests__gt=0), name='no_of_guests_gt_0'),
        ]

    def __str__(self):
        return f"{self.name} on {self.booking_date}"


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    inventory = models.IntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(inventory__gte=0), name='inventory_gte_0'),
        ]

    def __str__(self):
        return f"{self.title} - {self.price}"
