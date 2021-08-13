from django.urls import path

from . import views

app_name = "authentication"
urlpatterns = [
	path('', views.AuthenticationView, name='index'),

	#path('complete-sign-up/<str:username>/', views.CompleteSignUpView, name='complete_sign_up'),
	path('sign-in/', views.SignInView, name="sign_in"),
    path('sign-up/', views.SignUpView, name="sign_up"),
    path('sign-out/', views.SignOutView, name="sign_out"),
    path('reset-password/', views.PasswordResetView, name="reset_password"),
    path('lock-screen/', views.LockScreenView, name="lock_scrren"),
    path('forgot-password/', views.ForgotPasswordView, name="forgot_password"),
]
