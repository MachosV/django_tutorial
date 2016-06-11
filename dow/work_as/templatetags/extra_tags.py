from django import template
import random

register = template.Library()

@register.simple_tag()
def rand():
    return random.randint(-3,3)