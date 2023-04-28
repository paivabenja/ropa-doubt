from rest_framework import viewsets
from user.serializer import UserSerializer
from user.models import User


# Create your views here.
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
