from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)



# Creaing Router Objects
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('studentapi',views.StudentViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('refreshtoken/',TokenRefreshView.as_view(),name="token_refresh_pair"),
    path('verifytoken/',TokenVerifyView.as_view(),name="token_verify_pair"),
]