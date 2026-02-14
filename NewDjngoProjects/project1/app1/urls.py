from django.urls import path
from app1.views import welcome,login,logout

urlpatterns = [
    path('test/',welcome),
    path('login/',login),
    path('logout/',logout),

]
