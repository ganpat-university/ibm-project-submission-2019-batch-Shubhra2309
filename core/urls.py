from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import url_helper                      # import urls_helper module
import importlib
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import AdvancedSecurity
#urlpatterns = url_helper.get_urlpatterns()    # call get_urlpatterns() function to set urlpatterns variables
urlpatterns = [
            path("admin/", admin.site.urls, name='admin'),
            #path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
            path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
            path('', include('homepage.urls')),
            path('inventory/', include('inventory.urls')),
            path('transactions/', include('transactions.urls')),
            path('lockdown/', include('security.urls'),name='lockdown')
        ]
