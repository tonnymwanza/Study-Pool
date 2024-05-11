from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView
from drf_spectacular.views import SpectacularRedocView

# my url patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('', include('APIs.urls')),
    path('auth', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger/', SpectacularSwaggerView.as_view(), name='swagger'),
    path('schema/redoc', SpectacularRedocView.as_view(), name='redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
