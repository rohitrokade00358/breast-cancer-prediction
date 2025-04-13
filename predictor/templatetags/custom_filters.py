# predictor/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def replace(value):
    """
    Replaces underscores with spaces in the string value.
    Usage: {{ value|replace }}
    """
    return value.replace("_", " ")
