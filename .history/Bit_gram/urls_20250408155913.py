
from django.contrib import admin
from django.urls import path, include

from users.views import RegisterView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),
]
