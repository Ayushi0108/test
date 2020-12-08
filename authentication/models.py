from django.db import models
from django.utils.timezone import now
class Register(models.Model):
        name = models.CharField(max_length=30)
        email = models.EmailField(max_length=50,primary_key=True)
        password = models.CharField(max_length=15)


class Payment(models.Model):
        email = models.EmailField(max_length=50,null=False)
        prize = models.IntegerField()
        time = models.DateTimeField(default=now())