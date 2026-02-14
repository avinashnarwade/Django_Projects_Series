from django.contrib import admin
from django.urls import path,include
from app1.views import welcome
from app1.urls import login,logout
from app2.urls import add,sub
from app1.views import first,add1,add
from app3.views import add_view,home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/',include('app1.urls')),
    path('app2/',include('app2.urls')),
    path('app3/',include('app3.urls')),
    
    
    path('first/',first),
    path('add1/',add1),
    path('add/<int:n1>/<int:n2>/',add),
]


