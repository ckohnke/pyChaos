from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /chaos/
    url(r'^$', views.index, name='index'),
    
    url(r'^(?P<acronym_id>[0-9]+)/$', views.detail, name='detail'),
]
