from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Shopping Cart_Swagger')

main_urls = [
    path('admin/', admin.site.urls),
    path('api/', include('user.urls'))
]

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('', schema_view)
]
