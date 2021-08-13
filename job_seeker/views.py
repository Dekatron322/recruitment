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
def JobSeekerView(request):
	context = {}
	return render(request, "job/dashboard.html", context)

def ProfileView(request):
	context = {}
	return render(request, "job/profile.html", context)

def ProfileUpdateView(request):
	context = {}
	return render(request, "job/profile-update.html", context)
