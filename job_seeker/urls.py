from django.urls import path

from . import views

app_name = "job_seeker"
urlpatterns = [
	path('dashboard/', views.JobSeekerView, name='dashboard'),
    path('profile/', views.ProfileView, name='profile'),
    path('profile-update/', views.ProfileUpdateView, name='profile-update'),
]