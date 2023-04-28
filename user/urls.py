from django.urls import path, include
from rest_framework import routers
from user.views import UserView

router = routers.DefaultRouter()
router.register('user', UserView)

urlpatterns = [
    path('api/', include(router.urls))
]
