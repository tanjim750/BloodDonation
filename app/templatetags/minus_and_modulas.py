from django import template

register = template.Library()

@register.filter
def minus_and_modulas(num1,num2):
    num1 = int(num1)
    num2 = int(num2.split(':')[0])
    num3 = int(num2.split(':')[1])
    
    if num3> num1:
        num1 = num1-num3
        value = True if num1%num2 == 0 else False

    else:
        value = False

    print("modulas...", num1, num2,value)
    return value
