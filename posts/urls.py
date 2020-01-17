from django.urls import path
from . import views
urlpatterns = [
    path(r'index', views.index,name='index'),
    path(r'', views.note_traffic,name='traffic'),
    path(r'base_layout',views.base_layout,name='base_layout'),
    path(r'getdata',views.getdata,name='getdata')
]