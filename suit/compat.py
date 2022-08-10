import django

try:
    from importlib import import_module
except ImportError:  # python = 2.6
    from django.utils.importlib import import_module  # Django < 1.9

if django.VERSION[:2] < (1, 5):
    from django.templatetags.future import url
else:
    from django.template.defaulttags import url

try:
    from django.contrib.contenttypes import admin as ct_admin
except ImportError:
    from django.contrib.contenttypes import generic as ct_admin  # Django < 1.8

if django.VERSION[:2] < (1, 8):
    from django.template import Context

    tpl_context_class = Context
else:
    tpl_context_class = dict
