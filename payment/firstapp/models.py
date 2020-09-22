from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField(default='SOME STRING')
    amount = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    def __str__(self):
        return self.name
