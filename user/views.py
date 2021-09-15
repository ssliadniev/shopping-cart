from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model



class CurrentUserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
