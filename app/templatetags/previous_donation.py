from django import template
import datetime

register = template.Library()

@register.filter
def previous_donation(date):
    today = datetime.datetime.today().date()
    last_donation = (today - date).days

    return last_donation