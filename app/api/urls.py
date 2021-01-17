from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import AccountViewSet, TransactionViewSet

router_v1 = DefaultRouter()
router_v1.register('accounts', AccountViewSet, 'accounts')
router_v1.register('transactions', TransactionViewSet, 'transactions')

urlpatterns = [
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/', include(router_v1.urls)),
]