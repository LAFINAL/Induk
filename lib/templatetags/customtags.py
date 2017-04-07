from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def split(string, args):
    """
    Example usage: {{ value|split:"/,2" }}
    """
    # arg_list = [arg for arg in args.split(',')]
    # return string.split(arg_list[0])[int(arg_list[1])]
    return string.split(args)
