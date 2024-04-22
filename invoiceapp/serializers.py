from rest_framework import serializers
from models import InvoiceHeader, InvoiceItems, InvoiceBillSundry, Invoice


class InvoiceHeaderSerializer(serializers.Serializer):
    class Meta:
        model = InvoiceHeader
        fields = '__all__'

class InvoiceItemsSerializer(serializers.Serializer):
    class Meta:
        model = InvoiceItems
        fields = '__all__'


class InvoiceBillSundrySerializer(serializers.Serializer):
    class Meta:
        model = InvoiceBillSundry
        fields = '__all__'


class InvoiceSerializer(serializers.Serializer):
    invoice_header = serializers.SerializerMethodField(read_only=True)
    invoice_items = serializers.SerializerMethodField(read_only=True)
    invoice_sundry = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Invoice
        fields = ('__all__')

    def get_invoice_header(self, obj):
        header_map = InvoiceHeader.objects.get(invoice=obj)
        data = InvoiceHeaderSerializer(header_map.invoice_header).data
        return data

    def get_invoice_items(self, obj):
        invoice_items_map = InvoiceItems.objects.get(invoice=obj)
        data = InvoiceItemsSerializer(invoice_items_map, many=True).data
        return data

    def get_invoice_sundry(self, obj):
        bill_sundry = InvoiceBillSundry.objects.get(invoice=obj)
        data = InvoiceItemsSerializer(bill_sundry, many=True).data
        return data

