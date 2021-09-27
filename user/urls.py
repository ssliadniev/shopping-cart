from django.urls import path

from .views import CurrentUserRetrieveUpdateAPIView

urlpatterns = [
    path('', CurrentUserRetrieveUpdateAPIView.as_view()),
]
