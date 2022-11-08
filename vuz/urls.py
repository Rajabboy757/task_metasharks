from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

from vuz.views import UserViewSet, DirectionViewSet, GroupViewSet, SubjectViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

router1 = DefaultRouter()
router1.register(r'directions', DirectionViewSet)

router2 = DefaultRouter()
router2.register(r'group', GroupViewSet)

router3 = DefaultRouter()
router3.register(r'subject', SubjectViewSet)

urlpatterns = [
    # Your URLs...
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls + router1.urls + router2.urls + router3.urls
