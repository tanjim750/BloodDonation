from django import template

register = template.Library()

@register.filter
def modulas(num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    value = True if num1%num2 == 0 else False
    return value