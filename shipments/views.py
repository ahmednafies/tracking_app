import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from markdown import markdown

from shipments.forms import ShipmentForm
from shipments.models import Shipment


class AssignmentView(TemplateView):
    template_name = "shipments/assignment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        with open(os.path.join(settings.BASE_DIR, "README.md"), encoding="utf-8") as f:
            assignment_content = f.read()

        context.update({"assignment_content": mark_safe(markdown(assignment_content))})

        return context


class DashboardView(LoginRequiredMixin, ListView):
    model = Shipment
    ordering = ("shipping_date",)
    context_object_name = "shipments"
    template_name = "shipments/dashboard.html"

    def get_queryset(self):
        shipments = super().get_queryset()
        shipments = shipments.select_related("sender", "receiver")

        return shipments


class ShipmentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "shipments/shipment_form.html"
    model = Shipment
    form_class = ShipmentForm
    success_url = reverse_lazy("dashboard")
