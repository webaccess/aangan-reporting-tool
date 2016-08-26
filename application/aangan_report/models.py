from __future__ import unicode_literals

from datetime import datetime
from model_utils.models import TimeStampedModel

from django.db import models


class ScoringSchema(TimeStampedModel):
    uid = models.IntegerField(unique=True, blank=False, default=None)
    name = models.CharField(max_length=200, verbose_name ='Name')
    color = models.CharField(max_length=50, verbose_name='Color')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "scoring_schema"


class Category(TimeStampedModel):
    uid = models.IntegerField(unique=True, blank=False, default=None)
    name = models.CharField(max_length=300, verbose_name ='Category Name')
    description = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "category"


class Question(TimeStampedModel):
    uid = models.IntegerField(unique=True, blank=False, default=None)
    category = models.ForeignKey(Category, verbose_name ='Category Id')
    name = models.CharField(max_length=200, verbose_name ='Question Name')
    formula = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "question"


class ReportInstance(TimeStampedModel):
    doc = models.DateTimeField(default=datetime.now, verbose_name ='Date Of Creation')

    class Meta:
        db_table = "report_instance"


class QuestionInstance(TimeStampedModel):
    report_instance = models.ForeignKey(ReportInstance, verbose_name='Report Instance Id')
    question = models.ForeignKey(Question, verbose_name='Question Id')
    value = models.CharField(max_length=200, verbose_name='Value')

    class Meta:
        db_table = "question_instance"


class CategoryInstance(TimeStampedModel):
    report_instance = models.ForeignKey(ReportInstance, verbose_name='Report Instance Id')
    category = models.ForeignKey(Category, verbose_name='Category Id')
    value = models.CharField(max_length=200, verbose_name='Value')
    sugestion_text = models.TextField()

    class Meta:
        db_table = "category_instance"



