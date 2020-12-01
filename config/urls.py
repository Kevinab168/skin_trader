from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('skin_trader.users.urls')),
    path('api/token-auth/', obtain_auth_token),
    path('api/items/', include('skin_trader.items.urls')),
]
