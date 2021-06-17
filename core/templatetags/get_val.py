from django import template
from django.template.defaulttags import register

@register.filter
def get_val(dictionary,key):
    return dictionary.get(key)