from django import template

register = template.Library()

@register.filter
def call_my_function():
    pass