from django.conf.urls import url

from shipments.views import AssignmentView, DashboardView, ShipmentUpdateView


urlpatterns = [
    url(r'^$', AssignmentView.as_view(), name='assignment'),
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^shipments/(?P<pk>[0-9]+)-(?P<slug>[-\w]*)/$', ShipmentUpdateView.as_view(), name='shipment-update'),
]
