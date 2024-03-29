from django.db import models

class Stock(models.Model):

    ticker = models.CharField(max_length=10, unique=True,
                              blank=False, null=False)

    def __str__(self):
        return self.ticker