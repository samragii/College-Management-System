from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('courses/', include('courses.urls')),
    path('accounts/',include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('students.api_urls')),
    path('api/', include('courses.api_urls')),
    path('api/schema/',SpectacularAPIView.as_view(),name='schema'),
    path('api/docs/',SpectacularSwaggerView.as_view(url_name='schema'),
    name='swagger-ui',),
    path('api/', include('tasks.urls')),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )


