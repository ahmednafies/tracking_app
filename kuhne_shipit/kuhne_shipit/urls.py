
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    url(r'', include('auth.urls')),
    url(r'', include('shipments.urls')),
    url(r'^api/v1/', include('api.urls', namespace="api-v1"), name="api-v1"),
    url(r'^api/v2/', include('api_v2.urls', namespace="api-v2")),
    url(r'^token$', obtain_jwt_token, name='api-login'),
    url(r'^admin/', admin.site.urls),
]
