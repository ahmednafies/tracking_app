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
            'shipping_date',
            'delivery_date',
            'status'
        )

        read_only_fields = ["id"]
        required_fields = '__all__'

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    def validate_status(self, value):
        if not value:
            raise serializers.ValidationError("Status is not added")
        return value

    def validate_product(self, value):
        if not value:
            raise serializers.ValidationError("Product is not Supplied")
        return value

    def validate_shipping_date(self, value):
        if not value:
            raise serializers.ValidationError("Shipping Date is not Supplied")
        return value

    def get_shipping_date(self):
        request = self.context.get("request")
        date_string = request.data["shipping_date"]
        try:
            datetime_object = datetime.strptime(date_string, '%Y-%m-%d')
        except ValueError:
            raise serializers.ValidationError("Shipping Date is not Supplied")
        else:
            return datetime_object.date()

    def get_sender(self):
        request = self.context.get("request")
        return int(request.data["sender"])

    def validate_delivery_date(self, value):
        shipping_date = self.get_shipping_date()
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

