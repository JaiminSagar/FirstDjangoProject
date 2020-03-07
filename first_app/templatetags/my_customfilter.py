from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value,arg):
    """
    This cut out the alls values of the arg form the string!
    :param value:
    :param arg:
    :return:
    """

    return value.replace(arg, '')

# register.filter('cut', cut)