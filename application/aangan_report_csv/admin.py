from django.contrib import admin
from .models import SurveyOne, SurveyTwo


class SurveyOneAdmin(admin.ModelAdmin):
    list_display = [f.name for f in SurveyOne._meta.fields]


class SurveyTwoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in SurveyTwo._meta.fields]


admin.site.register(SurveyOne, SurveyOneAdmin)
admin.site.register(SurveyTwo, SurveyTwoAdmin)