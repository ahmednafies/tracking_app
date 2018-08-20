from django.contrib.auth.models import User
from rest_framework import serializers
from shipments.models import Company, Shipment


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer Class for Users
    """
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'is_staff'
        )


class CompanySerializer(serializers.ModelSerializer):
    """
    Serializer class for Companies
    """
    class Meta:
        model = Company
        fields = '__all__'


class ShipmentSerializer(serializers.ModelSerializer):
    """
    Serializer class for shipments
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

        read_only_fields = ['id', ]

        def validate_tracking_no(self, value):
            """
            method checks if tracking number is used,
            raises a ValueError if True
            :param value: tracking_no
            :return: tracking_no
            """
            qs = Shipment.objects.filter(tracking_no__iexact=value)
            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise serializers.ValidationError("Tracking number is already used")
            return value

        def validate_sender(self, value):
            """
            Method Checks if sender and receiver are equal,
            Raises a ValueError if True
            :param value: sender
            :return:
            """
            if value == self.instance.receiver:
                raise serializers.ValidationError("Sender and Reciever cannot be the same")
            return value
