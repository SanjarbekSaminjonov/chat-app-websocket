from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('chat/<str:room_name>/', views.room_view, name='room')
]
