from django import template

register = template.Library()

@register.filter
def linebreak(text:str):
    text = text.replace('\n','<br><br>')
    return text