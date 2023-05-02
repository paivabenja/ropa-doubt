from rest_framework import routers
from clothes.views import ClothesView
from django.urls import path, include

router = routers.DefaultRouter()
router.register("api", ClothesView)

urlpatterns = [path("", include(router.urls))]
