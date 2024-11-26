from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('register/', views.registerUser, name="register"),
    path('login/', views.login_user, name='login'),
    path("logout/", views.logoutUser, name="logout"),
]
