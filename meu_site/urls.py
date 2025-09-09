#meu_site/urls.py
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
#import static
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', include('agenda.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)