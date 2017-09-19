from django.conf.urls import url
from django.contrib import admin
from posts.views import post_create, post_list, post_detail, post_update, post_delete

urlpatterns = [
    url(r'^$', post_list),  # Posts url Default
    url(r'^create/$', post_create),
    url(r'^list/$', post_list),
    url(r'^(?P<id>\d+)/$', post_detail),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),
]