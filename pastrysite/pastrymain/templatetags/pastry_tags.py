from django import template
from pastrymain.models import *

register = template.Library()

@register.simple_tag(name='get_categories')
def get_categories(filter=None):
    if not filter:
        return Categories.objects.all()
    else:
        return Categories.objects.filter(pk=filter)


@register.inclusion_tag('pastrymain/list_categories.html')
def show_categories(sort=None, category_selected=0):
    if not sort:
        categories = Categories.objects.all()
    else:
        categories = Categories.objects.order_by(sort)
    
    return {'categories': categories, 'category_selected': category_selected}

