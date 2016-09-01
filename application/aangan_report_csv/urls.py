from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^upload-csv-one/$', views.upload_survey_one, name='upload-csv-one'),
    url(r'^upload-csv-two/$', views.upload_survey_two, name='upload-csv-two'),
]