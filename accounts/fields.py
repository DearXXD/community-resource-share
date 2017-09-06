# coding:utf-8
from django.db.models.fields import CharField,TextField
from django.db import models
import ast
import json
from rest_framework import serializers

class ListField(TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        # kwargs['max_length'] =
        super(ListField, self).__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection, context):
        if not value:
            value = []

        if isinstance(value, list):
            value.sort()
            return value
        return ast.literal_eval(value)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            value.sort()
            return value
        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value
        if isinstance(value, list):
            value.sort()
            return unicode(value)
        return unicode(value)  # use str(value) in Python 3

class DictArrField(TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(DictArrField, self).__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection, context):
        if not value:
            value = []

        if isinstance(value, list):
            value.sort()
            return value
        return json.loads(value)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            value.sort()
            return value
        return json.loads(value)

    def get_prep_value(self, value):
        if value is None:
            return value
        if isinstance(value, list):
            value.sort()
            return json.dumps(value)
        return str(value)  # use str(value) in Python 3

