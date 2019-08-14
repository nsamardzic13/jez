from django import  template
import os
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def split_name(value):
    return os.path.basename(str(value))

@register.simple_tag()
def define():
     return None

@register.simple_tag()
def change(val=None):
  return val
