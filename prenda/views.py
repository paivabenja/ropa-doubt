from rest_framework import viewsets
from prenda.serializer import PrendaSerializer
from prenda.models import Prenda


# Create your views here.
class PrendaView(viewsets.ModelViewSet):
    serializer_class = PrendaSerializer
    queryset = Prenda.objects.all()
