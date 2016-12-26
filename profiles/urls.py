from django.conf.urls import url
from . import views

app_name='profiles'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name='index'),

    #url(r'^task/(?P<pk>[0-9]+)$',views.SubIndexView.as_view(),name='detail'),
    #url(r'^(?P<task_details>[0-9]+)$',views.detail,name='detail'),

	url(r'^(?P<pk>[0-9]+)$',views.DetailView.as_view(),name='detail'),

    url(r'^task/add/$',views.TaskCreate.as_view(),name='task-add'),

    url(r'^task/(?P<pk>[0-9]+)$',views.TaskUpdate.as_view(), name='task-update'),

    url(r'^task/(?P<pk>[0-9]+)/delete/$',views.TaskDelete.as_view(), name='task-delete'),

    url(r'^task/add_sub/$',views.SubTaskCreate.as_view(),name='subtask-add'),
]

