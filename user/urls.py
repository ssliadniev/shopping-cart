from django.urls import path

from .views import CurrentUserRetrieveUpdateAPIView

app_name = "user"

urlpatterns = [
    path('', CurrentUserRetrieveUpdateAPIView.as_view(), name="user"),
]
