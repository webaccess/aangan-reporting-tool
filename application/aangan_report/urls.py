from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^generate-report/$', views.index, name='generate-report'),

]