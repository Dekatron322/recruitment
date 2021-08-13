from django.urls import path

from . import views

app_name = "employer"
urlpatterns = [
    path('profile/', views.CompanyProfileView, name='profile'),
    path('profile-update/', views.ProfileUpdateView, name='profile-update'),
]