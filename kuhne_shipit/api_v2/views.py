from rest_framework import generics
from rest_framework import mixins
from shipments.models import Shipment
from shipments.models import Company
from api_v2.serializers import ShipmentSerializer
from api_v2.serializers import CreateShipmentSerializer
from api_v2.serializers import CompanySerializer


# ----------------------------------------------- Company API Views ------------------------------------------------- #

class CompanyAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    """
    Create, List Companies
    """
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request":self.request}
# ----------------------------------------------- Company RUD Views ------------------------------------------------- #

class CompanyByIdRudView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for Retrieve, Update, Delete Companies by Id
    """
    lookup_field = "pk"
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request":self.request}


# ----------------------------------------------- Shipment API Views ------------------------------------------------- #


class ShipmentAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    """
    Create, List Shipments
    """
    lookup_field = "pk"
    serializer_class = CreateShipmentSerializer
    queryset = Shipment.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request":self.request}
# ----------------------------------------------- Shipment RUD Views ------------------------------------------------- #


class ShipmentByIdRudView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for Retrieve, Update, Delete Shipments by Id
    """
    lookup_field = "pk"
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request":self.request}

class ShipmentByTrackingNoRudView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for Retrieve, Update, Delete Shipments by tracking_no
    """
    lookup_field = "tracking_no"
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request":self.request}