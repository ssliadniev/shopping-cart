from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view


main_urls = [
    path('user/', include('user.urls', namespace="user")),
    path('products/', include('products.urls'))
]

schema_view = get_swagger_view(title="Shopping Cart Swagger")
urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(main_urls)),
    path('swagger/', schema_view),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
