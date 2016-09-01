from django.contrib import admin
from .models import ScoringSchema, Category, Question, \
    ReportInstance, QuestionInstance, CategoryInstance


class ScoringSchemaAdmin(admin.ModelAdmin):
    list_display = ('id', 'uid', 'name', 'color')
    # list_filter = ('')
    # search_fields = ('')
    # ordering = ('')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'uid', 'name', 'description')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'uid', 'category', 'name', 'formula')


class ReportInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'doc')


class QuestionInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'report_instance', 'question', 'value')


class CategoryInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'report_instance', 'category', 'value', 'sugestion_text')


# Register the new EmailUserAdmin
admin.site.register(ScoringSchema, ScoringSchemaAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(ReportInstance, ReportInstanceAdmin)
admin.site.register(QuestionInstance, QuestionInstanceAdmin)
admin.site.register(CategoryInstance, CategoryInstanceAdmin)
