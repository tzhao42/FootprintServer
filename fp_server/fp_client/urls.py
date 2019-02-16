from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/<str:email_in>/<str:password_in>/', views.login, name='user'),
    #path('add_trip/', views.add_trip, name='add_trip')
    path('fetch_user_trips/<int:user_id_in>/', views.fetch_user_trips, name='fetch_user_trips'),
    path('fetch_comm_trips/<str:lat_str_in>/<str:long_str_in/>', views.fetch_comm_trips, name='fetch_comm_trips'),
]
