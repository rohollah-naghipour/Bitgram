
from django.urls import path

from users.views import RegisterView, GeneratePassView



urlpatterns = [
    path('api/register/', RegisterView.as_view(), name = 'register'),

    path('api/gen_password/<int:num>/', GeneratePassView.as_view(), name = 'gen_pass'),
]