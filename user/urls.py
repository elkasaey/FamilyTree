from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/token', views.CustomTokenView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh', views.CustomTokenView.as_view(), name='token_refresh'),
    path('create', views.createUser, name='createUser'),
]
