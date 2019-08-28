from django import  template
import os
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def split_name(value):
    return os.path.basename(str(value))

@register.filter(name='times')
def times(number):
    return range(number)

@register.filter(name='add')
def add(number):
    return number+1

@register.simple_tag()
def check_sem(value):
    return value+1

@register.simple_tag()
def check_image(value):
    name, extension = os.path.splitext(str(value))
    if extension == ".jpg" or extension == ".png" or extension == ".svg":
        return True
    return False

@register.simple_tag()
def define():
     return None

@register.simple_tag()
def change(val=None):
  return val
