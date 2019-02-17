"""fp_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path

import fp_client.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fp_client.views.index, name='index'),
    path('signup/', fp_client.views.signup, name='signup'),
    path('login/', fp_client.views.login, name='login'),
    path('add_trip/', fp_client.views.add_trip, name='add_trip'),
    path('fetch_user_trips/', fp_client.views.fetch_user_trips, name='fetch_user_trips'),
    path('fetch_comm_trips/', fp_client.views.fetch_comm_trips, name='fetch_comm_trips'),
    path('stats/', fp_client.views.stats, name='stats'),
    path('community/', fp_client.views.community, name='community')
]










