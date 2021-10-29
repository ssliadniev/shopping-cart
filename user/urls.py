from django.urls import path

from user.views import CurrentUserRetrieveUpdateAPIView


app_name = "user"

urlpatterns = [
    path('', CurrentUserRetrieveUpdateAPIView.as_view(), name="retrieve-update"),
]
