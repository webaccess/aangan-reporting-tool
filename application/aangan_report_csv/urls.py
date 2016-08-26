from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^upload_csv/$', views.upload_survey_one, name='upload_csv'),
    url(r'^upload_csv_two/$', views.upload_survey_two, name='upload_csv_two'),

]