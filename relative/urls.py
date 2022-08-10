from django.urls import path, include

from rest_framework import routers
# from rest_framework_extensions import routers

from . import views

router =  routers.DefaultRouter()
router.register(r'family',views.RelativeViewSet)

router.register(r'children',
                views.RelativeViewSet)

router.register(r'parents',
                views.ParentViewSet)

router.register(r'siblings',
                views.SiblingViewSet)

urlpatterns = [
    path(r'^', include(router.urls)),
]
