from django.contrib import admin
from django.urls import path

from .views import CurrentUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/user/', CurrentUser.as_view()),
]
