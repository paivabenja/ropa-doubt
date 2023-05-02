from rest_framework import viewsets
from clothes.serializer import ClothesSerializer
from clothes.models import Clothes


# Create your views here.
class ClothesView(viewsets.ModelViewSet):
    serializer_class = ClothesSerializer
    queryset = Clothes.objects.all()
