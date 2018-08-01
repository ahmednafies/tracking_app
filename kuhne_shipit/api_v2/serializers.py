from rest_framework import serializers
from shipments.models import Company
from shipments.models import Shipment
from datetime import datetime
# ------------------------------------------- Company Serializers -----------------------------------------------------#


class CompanySerializer(serializers.ModelSerializer):
    """
    Serializer class for Companies
    """
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Company
        fields = (
            'id',
            'url',
            'name',
            'address'
        )

        read_only_fields = ["id"]

    # this method is used to get the full URL of instance
    # it is used for both API and Testing
    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)
# ------------------------------------------ Shipment Serializers -----------------------------------------------------#


class CreateShipmentSerializer(serializers.ModelSerializer):
    """
    Serializer class for shipment Creation
    """
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Shipment
        fields = (
            'id',
            'url',
            'tracking_no',
            'sender',
            'receiver',
            'product',
            'delivery_date',
            'shipping_date',
            'status'
        )

        read_only_fields = ["id"]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    def get_shipping_address(self):
        request = self.context.get("request")
        date_string = request.data["shipping_date"]
        datetime_object = datetime.strptime(date_string, '%Y-%m-%d')
        return datetime_object.date()

    def get_sender(self):
        request = self.context.get("request")
        return int(request.data["sender"])

    def validate_delivery_date(self, value):
        shipping_date = self.get_shipping_address()
        if value <= shipping_date:
            raise serializers.ValidationError("Delivery Date must be after Shipping Date")
        return value

    def validate_receiver(self,value):
        sender = self.get_sender()
        if value.id == sender:
            raise serializers.ValidationError("Sender and Receiver cannot be the same")
        return value

class ShipmentSerializer(serializers.ModelSerializer):
    """
    Serializer Class to retrieve, Update or Destroy Shipments
    """

    class Meta:
        model = Shipment
        fields = (
            'id',
            'tracking_no',
            'sender',
            'receiver',
            'product',
            'delivery_date',
            'shipping_date',
            'status'
        )

        read_only_fields = ["id", "tracking_no", "sender", "product", "shipping_date"]

    def validate_delivery_date(self, value):
        qs = Shipment.objects.get(pk=self.instance.pk)
        if value <= qs.shipping_date:
            raise serializers.ValidationError("Delivery Date must be after Shipping Date")
        return value

    def validate_receiver(self,value):
        qs = Shipment.objects.get(pk=self.instance.pk)
        if value == qs.sender:
            raise serializers.ValidationError("Sender and Receiver cannot be the same")
        return value

    def validate_status(self, value):
        qs = Shipment.objects.get(pk=self.instance.pk)
        if qs.status == "Delivered":
            raise serializers.ValidationError("The shipment is already delivered, cannot change it anymore")
        return value

