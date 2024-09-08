from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView

from houses.urls import urlpatterns as houses_urls

app_name = 'api'

urlpatterns = [
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]

urlpatterns += houses_urls
