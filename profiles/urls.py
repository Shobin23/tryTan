from django.conf.urls import url
from . import views

app_name='profiles'

urlpatterns = [
    url(r'^$', views.index,name='index'),

    url(r'^(?P<task_details>[0-9]+)$',views.detail,name='detail'),
]
''