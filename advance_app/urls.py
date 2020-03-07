from django.conf.urls import url
from django.urls import re_path, path
from advance_app import views

app_name = 'advance_app'

urlpatterns = [
    url(r'^$', views.index, name="advance_index"),
    url(r'^ex_view_class/', views.cbv_View.as_view(), name='cbv_View'),
    url(r'^ex_tempView_class/', views.cbv_tempView.as_view(), name='cbv_TemplateView'),
    url(r'^school_list/$', views.SchoolListView.as_view(), name='school_view'),
    url(r'^school_list/(?P<pk>\d+)/$',views.SchoolDetailView.as_view(), name='school_detail'),
    url(r'^create/$', views.SchoolCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.SchoolDeleteView.as_view(), name='delete'),
    #path('update/<int:pk>/',views.SchoolUpdateView.as_view(),name='update'),
]