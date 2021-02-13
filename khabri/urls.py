"""khabri URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from newsapp.views import *
from django.contrib.auth import views as auth_views
from .import settings

router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'news', NewsAppViewSet, basename='news')
router.register(r'marque',MarqueViewSet,basename='marque')
urlpatterns = router.urls

urlpatterns += [
    path('admin/backups/', include('dbbackup_ui.urls')),  
    path('admin/password_reset/',auth_views.PasswordResetView.as_view(),name='admin_password_reset'),
    path('admin/password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(success_url='/login/'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='login.html',success_url = '/login/?success=Password reset link sent to your given email id'),name='change_password'),
    path('admin/', admin.site.urls),
    path('videos/',VideoLinkView.as_view()),
    path('videonews/',VideoNewsView.as_view()),
    path('sliderads/',AdvertismentView.as_view()),
    path('preview/<id>/',PreviewView,name='preview')
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)