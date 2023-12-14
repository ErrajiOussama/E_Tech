from django.urls import path
from . import views


urlpatterns = [
    path('register-login/',views.loginRegisterPageView,name="login-register"),
    path('logout/',views.logoutview,name='logout'),
]
