from django.shortcuts import render
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
# Create your views here.


def index(request):
	context = {}
	
	return render(request, "landing_page/index.html", context )
