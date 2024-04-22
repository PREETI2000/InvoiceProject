from django.http import JsonResponse
from django.shortcuts import render
import requests
# Create your views here.
from invoiceapp.models import Invoice
from serializers import InvoiceHeaderSerializer, InvoiceItemsSerializer, InvoiceBillSundrySerializer,InvoiceSerializer
from models import InvoiceHeader, InvoiceItems, InvoiceBillSundry, Invoice


def invoice(request):
    if request.method == 'POST':
        valid, msg = validate_data(request)
        if not valid:
            return 'Failure'
        data = request.data
        invoice = InvoiceSerializer(data=data['invoice'])
        header = InvoiceHeaderSerializer(data=data['invoice_header'], context={'invoice':invoice})
        item = InvoiceItemsSerializer(data=data['invoice_items'])
        bill_sundry = InvoiceBillSundrySerializer(data=data['bill_sundry'])
        return 'Success!'
    if request.method == 'GET':
        invoice_id = request.GET.get('id')
        if invoice_id:
            invoice = Invoice.objects.get(id=id)
            data = InvoiceSerializer(invoice).data
        else:
            invoice = Invoice.objects.all()
            data = InvoiceSerializer(invoice, many=True).data
        return data
    # if request is to delete
    if request.method == 'DELETE':
        invoice_id = request.GET['id']
        obj = Invoice.objects.get(id=id)
        InvoiceHeader.objects.get(invoice=obj).delete()
        InvoiceItems.objects.get(invoice=obj).delete()
        InvoiceBillSundry.objects.get(invoice=obj).delete()
        Invoice.objects.get(id=id).delete()
    # if request is to update the data
    if request.method == 'PUT':
        invoice_id = request.GET['id']
        obj = Invoice.objects.get(id=id)


def validate_data(request):
    if 'invoice_header' not in request.data:
        return JsonResponse('Header missing')
    if not request['invoice_header']:
        return JsonResponse('Header values missing')
    if 'invoice_items' not in request.data:
        return JsonResponse('Items missing')
    if 'bill_sundry' not in request.data:
        return JsonResponse('Bill  missing')
