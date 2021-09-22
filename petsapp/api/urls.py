
from django.urls import path

from petsapp.api import views

urlpatterns = [
    path('account/register/', views.AccountRegisterView.as_view()),
    path('account/login/', views.login_view),
]