from django.contrib import admin
from .models import ScoringSchema, Category, Question, \
    ReportInstance, QuestionInstance, CategoryInstance

admin.site.register(ScoringSchema)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(ReportInstance)
admin.site.register(QuestionInstance)
admin.site.register(CategoryInstance)