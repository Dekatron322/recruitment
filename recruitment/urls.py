"""recruitment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from landing_page import views
from authentication import views as AuthenticationViews
from job_seeker import views as JobSeekerViews
from recruitement_agency import views as RecruitmentAgencyViews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing_page.urls')),
    path('authentication/', include('authentication.urls')),
    path('job_seeker/', include('job_seeker.urls')),
    path('recruitement_agency/', include('recruitement_agency.urls')),
    path('employer/', include('employer.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
