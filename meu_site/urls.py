# meu_site/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from agenda.views import register_user # Importe a nova view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', include('agenda.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register_user, name='register'), # Nova URL para registro
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)