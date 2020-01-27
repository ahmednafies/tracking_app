from django.conf.urls import url
from api_v2.views import ShipmentByIdRudView
from api_v2.views import ShipmentByTrackingNoRudView
from api_v2.views import ShipmentAPIView
from api_v2.views import CompanyAPIView
from api_v2.views import CompanyByIdRudView


urlpatterns = [

    url(
        r'^companies/$',
        CompanyAPIView.as_view(),
        name='Create-List-Companies'
    ),

    url(
        r'^companies/id=(?P<pk>\d+)/$',
        CompanyByIdRudView.as_view(),
        name='RUD-Company-By-ID'
    ),

    url(
        r'^shipments/$',
        ShipmentAPIView.as_view(),
        name='Create-List-Shipments'
    ),

    url(
        r'^shipments/id=(?P<pk>\d+)/$',
        ShipmentByIdRudView.as_view(),
        name='RUD-Shipment-By-ID'
    ),

    url(
        r'^shipments/tracking_no=(?P<tracking_no>\w+)/$',
        ShipmentByTrackingNoRudView.as_view(),
        name='RUD-Shipment-By-Tracking-No'
    ),

]
