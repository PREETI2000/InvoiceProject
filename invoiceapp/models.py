from django.db import models


# Create your models here.
class Invoice(models.Model):
    name = models.CharField()
    uuid = models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class InvoiceHeader(models.Model):
    date = models.CharField()
    invoice_number = models.IntegerField()
    customer_name = models.CharField(max_length=128)
    billing_address = models.TextField()
    shipping_address = models.TextField()
    GSTIN = models.CharField()
    total_amount = models.IntegerField()
    invoice = models.ForeignKey(Invoice, on_delete=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class InvoiceItems(models.Model):
    itemName = models.CharField()
    quantity = models.FloatField()
    price = models.FloatField()
    amount = models.FloatField()
    invoice = models.ForeignKey(Invoice, on_delete=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class InvoiceBillSundry(models.Model):
    billSundryName = models.CharField()
    amount = models.FloatField()
    invoice = models.ForeignKey(Invoice, on_delete=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

