
from django.contrib import admin
from django.urls import path, include

from users.urls import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),

    path('',include('users.urls'))
]
