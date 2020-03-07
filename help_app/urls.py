from django.conf.urls import url
from help_app import views

urlpatterns = [
    url(r'^$', views.index, name = 'index_help')
]