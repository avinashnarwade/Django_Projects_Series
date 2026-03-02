from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/',admin.site.urls),
    path('accounts/',include('accounts_app1.urls')),
    path('profile/',include('profiles_app2.urls')),
    path('',include('dashboard_app3.urls')),
]
