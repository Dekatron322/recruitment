from django.shortcuts import render
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
# Create your views here.


def ProfileView(request):
	context = {}
	
	return render(request, "agency/profile.html", context)


def ProfileUpdateView(request):
	context = {}

	return render(request, "agency/update_profile.html", context)


def OneTimePaymentView(request):
	context = {}

	return render(request, "agency/payment.html", context)

def AdsPackageView(request):
	context = {}

	return render(request, "agency/packages.html", context)

def QuizView(request):
	pass

def OnlineInterView(request):
	pass
