from django.contrib.auth.models import User
from django.contrib.auth import get_user
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer


class CurrentUserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
   # queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return get_user(self.request)

