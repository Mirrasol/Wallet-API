from django.db import models


class Wallets(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, unique=True)
    balance = models.DecimalField(max_digits=15, decimal_places=3, default=0.000)

    def __str__(self):
        return f'Wallet {self.uuid}'
