from django.conf.urls import url
from . import views

app_name='profiles'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name='index'),

    #url(r'^(?P<task_details>[0-9]+)$',views.detail,name='detail'),
	url(r'^(?P<pk>[0-9]+)$',views.DetailView.as_view(),name='detail'),
]

