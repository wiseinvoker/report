"""teamreport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter
from report.views import ReportViewSet, LoginView, LogoutView, ProfileView, ReportListViewSet
from .views import IndexView

router = DefaultRouter()
# Property routes
router.register(r'reports', ReportViewSet)
router.register(r'reports-list', ReportListViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls), name='api'),
    url(r'^auth/login$', LoginView.as_view(), name='login'),
    url(r'^auth/logout$', LogoutView.as_view(), name='logout'),
    url(r'^auth/me$', ProfileView.as_view(), name='profile'),
    url(r'^$', IndexView.as_view()),
    url(r'^.*$', IndexView.as_view()),
]
