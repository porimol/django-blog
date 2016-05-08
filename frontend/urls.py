from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<post_id>[0-9]+)/single/$', views.signle_post, name='signle_post'),
]