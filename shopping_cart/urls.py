from django.contrib import admin
from django.urls import path, include


main_urls = [
    #path('api/', )
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
]
