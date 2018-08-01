from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from rest_framework.reverse import reverse as api_reverse

class Company(models.Model):

    class Meta:
        verbose_name_plural = "companies"

    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.name

    def get_api_url(self, request=None):
        return api_reverse("api-v2:RUD-Company-By-ID", kwargs={'pk': self.pk}, request=request)

class Shipment(models.Model):
    DELIVERY_STATUS = (
        ('Shipped', 'Shipped'),
        ('In Transit', 'In Transit'),
        ('Delivered', 'Delivered'),
    )

    tracking_no = models.CharField(max_length=128, unique=True)
    sender = models.ForeignKey('shipments.Company', on_delete=models.PROTECT)
    receiver = models.ForeignKey('shipments.Company', on_delete=models.PROTECT, related_name='shipments')
    product = models.CharField('Product', max_length=128, blank=True, null=True)
    shipping_date = models.DateField('shipping date', blank=True, null=True)
    delivery_date = models.DateField('Expected delivery date', blank=True, null=True)
    status = models.CharField(max_length=20, choices=DELIVERY_STATUS, blank=True, null=True)

    def __str__(self):
        return self.tracking_no

    def get_absolute_url(self):
        return reverse('shipment-update', kwargs={'pk': self.pk, 'slug': slugify(self.tracking_no)})

    def get_api_url(self, request=None):
        return api_reverse("api-v2:RUD-Shipment-By-ID", kwargs={'pk': self.pk}, request=request)


    @property
    def get_start_date(self):
        return self.shipping_date

    @property
    def get_end_date(self):
        return self.delivery_date

