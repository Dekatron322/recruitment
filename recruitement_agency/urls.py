from django.urls import path
from . import views

app_name = "recruitement_agency"
urlpatterns = [
	path('profile/', views.ProfileView, name='profile'),
    path('profile_update/', views.ProfileUpdateView, name='profile_update'),
    path('payment/', views.OneTimePaymentView, name='payment'),
    path('upgrade/', views.AdsPackageView, name='upgrade'),
    path('interview/', views.OnlineInterView, name='interview'),
    path('set_quiz/', views.QuizView, name='set_quiz'),

]