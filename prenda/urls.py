from django.urls import path, include
from rest_framework import routers
from prenda.views import PrendaView

router = routers.DefaultRouter()
router.register('prenda', PrendaView)

urlpatterns = [
    path('api/', include(router.urls))
]
