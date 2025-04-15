
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from users.urls import *
from posts.urls import *
from .local_settings import *

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', include('users.urls')),
    path('', include('posts.urls')),
    path('', include('posts.urls')),
]


if settings.DEVEL:
    urlpatterns += static('/media', document_root=settings.MEDIA_ROOT)