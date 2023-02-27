from django.db import models

# Create your models here.

PAYMENT_METHODS = [
    ('rev', 'Revolut'),
    ('ing', 'ING'),
]


class Spending(models.Model):
    location = models.CharField(max_length=18)
    amount = models.CharField(max_length=6)
    description = models.CharField(max_length=30)
    paid_with = models.CharField(max_length=7, choices=PAYMENT_METHODS)

    def __str__(self):
        return f'{self.location}->{self.amount}->{self.description}->{self.paid_with}'
