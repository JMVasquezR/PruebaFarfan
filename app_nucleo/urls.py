from django.conf.urls import url, include

urlpatterns = [
    url(r'^api/', include('app_nucleo.api.urls')),
]
