from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import AdvancedSecurity

def get_urlpatterns():
    if AdvancedSecurity.GLOBAL_LOCKDOWN == True:
        return [
            path("admin/", admin.site.urls, name='admin'),
            path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
            path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
            path('', include('security.urls')),
            path('inventory/', include('inventory.urls')),
            path('transactions/', include('transactions.urls')),
            path('lockdown/', include('security.urls'))
        ]
    else:
        return [
            path('', include('security.urls'))
        ]
