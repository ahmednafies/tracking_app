from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from api.views import UserViewSet, ShipmentViewSet, CompanyViewSet

router: DefaultRouter = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'shipments', ShipmentViewSet)
router.register(r'companies', CompanyViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='Apiv1-Auth')),
]

