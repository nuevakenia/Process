from django import template

@register.filter
def get_val(dictionary,value):
    
    return dictionary.get(value)