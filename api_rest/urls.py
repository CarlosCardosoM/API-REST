from django.urls import path
from .views import monografias_list, monografia_detail
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('monografias/', monografias_list, name='monografias-list'),
    path('monografias/<int:pk>/', monografia_detail, name='monografia-detail'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
