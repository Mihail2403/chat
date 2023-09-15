from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('reg/', views.register, name='reg'),
    path("login/", LoginView.as_view(template_name='account/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    # path('profile/', views.profile, name='profile'),
]
