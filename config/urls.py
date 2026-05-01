from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI

from portfolio.api import router as portfolio_router
from contact.api import router as contact_router

api = NinjaAPI(
    title='Shubber SB API',
    version='1.0.0',
    description='Backend API for Shubber SB Portfolio Website',
)

api.add_router('/portfolio', portfolio_router, tags=['Portfolio'])
api.add_router('/contact', contact_router, tags=['Contact'])

urlpatterns = [
    path('api/', api.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
