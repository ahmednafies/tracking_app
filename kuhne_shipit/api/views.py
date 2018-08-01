from django.contrib.auth.models import User
from rest_framework import viewsets, generics, permissions
from shipments.models import Company, Shipment
from api.serializers import CompanySerializer, ShipmentSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    """
    User Viewsets
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class CompanyViewSet(viewsets.ModelViewSet):
    """
    Company Viewsets
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAdminUser,
    )


class ShipmentViewSet(viewsets.ModelViewSet):
    """
    Shipment ViewSets
    """
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
