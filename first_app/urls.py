from django.conf.urls import url
from first_app import views

app_name = 'first_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^display/', views.display, name='display'),
    url(r'^display_users/', views.display_users, name='display_users'),
    url(r'^forms/', views.form_name_view, name='form_name'),
    url(r'^signup/', views.sign_up, name='sign_up'),
    url(r'^register/', views.register, name="register"),
    url(r'^navbar/', views.navbar, name="navbar")
]