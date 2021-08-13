from django.shortcuts import render
#from .forms import UserForm


from django.contrib import messages

from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.
def AuthenticationView(request):
	pass

def SignInView(request):
	context = {}
	return render(request, "auth/signin.html", context)




def SignUpView(request):
	context = {}
	return render(request, "auth/signup.html", context)

def LockScreenView(request):
	context = {}
	return render(request, "auth/lock-screen.html", context)

def PasswordResetView(request):
	context = {}
	return render(request, "auth/reset-password.html", context)

def ForgotPasswordView(request):
	context = {}
	return render(request, "auth/forgot-password.html", context)

def OneTimePaymentView(request):
	context = {}
	return render(request, "auth/payment.html", context)

def SignOutView(request):
	logout(request)

	return HttpResponseRedirect(reverse("landing_page:index"))



