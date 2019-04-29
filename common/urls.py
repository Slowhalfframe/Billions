from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_child_menu/$', views.get_child_menu, name='get_child_menu'),
]
