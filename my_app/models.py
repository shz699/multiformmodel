from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.
class Billing(models.Model):
    type = models.CharField(max_length=15)

    def __str__(self):
        return self.type


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=150 , null=True , blank=True)
    age = models.IntegerField(default=18)
    phone = models.CharField(max_length=20 , default='+880' , unique=True)
    billing = models.ForeignKey("Billing", on_delete=models.CASCADE)
    project = models.ForeignKey('Project' , on_delete=models.CASCADE , null=True , blank= True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['full_name']    


    def save(self , *args, **kwargs):
        self.full_name = self.first_name + ' ' + self.last_name
        return super().save(*args, **kwargs)    


class Project(models.Model):
    name = models.CharField(max_length=150)    
    address = models.CharField(max_length=150)  

    def __str__(self):
        return self.name


class PaymentType(models.Model):
    name = models.CharField(max_length=50)


    
    def __str__(self):
        return self.name

class Account(models.Model):
    billing = models.ForeignKey("Billing", on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    client = models.ForeignKey(Client , related_name='client', on_delete=models.CASCADE , null=True , blank=True)
    transaction_id = models.CharField(max_length=400 , unique=True)
    invoice_no = models.CharField(max_length=100 , unique=True)
    type = models.ForeignKey(PaymentType , on_delete=CASCADE)

    def __str__(self):
        return f'{self.billing.type} | {self.date} ; Payed by {self.client}'

