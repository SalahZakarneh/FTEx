from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^app/$', views.item_list),
    url(r'^app/(?P<pk>[0-9]+)/$', views.item_detail),
]