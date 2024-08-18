"""
URL configuration for ConsultClient project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,re_path
from . import views
urlpatterns = [
    path('', views.index, name="Dashboard" ),
    path('datatable/', views.datatable, name="datatable"),
    path('forms/',views.forms,name="forms"),
    path('forms-send',views.formSend,name="formSend"),
    path('forms-send/',views.formsSave,name="formsSave"),
    path('Mes-dossier/',views.mesdossier,name="mesdossier"),
    path('datatable-dossier/',views.datadossier,name="datadossier"),
    re_path(r'^data-avocat/(?P<id>\w+)/$',views.dataAvocat,name="dataAvocat"),
    re_path(r'^affecter-dossier/(?P<id>\w+)/$',views.sendDate,name="sendDate"),
    # re_path(r'^affecter-dossier/(?P<id>\w+)/$', views.sendDate,name="sendDate"),

]