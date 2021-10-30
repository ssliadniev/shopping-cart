from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from user.models import User
from user.serializers import UserSerializer


class CurrentUserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'patch']

    def get_object(self):
        return get_object_or_404(self.queryset, id=self.request.user.id)
