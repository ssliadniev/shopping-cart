from django.contrib import admin
from django.urls import path, include


main_urls = [
    path('admin/', admin.site.urls),
    path('api/', include('user.urls'))
]

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls'))
]
