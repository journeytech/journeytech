'''
Created on Sep 21, 2013

@author: antipro
'''
from django import template
from django.forms.fields import DateField, DateTimeField

register = template.Library()


@register.inclusion_tag("general/form_requirement.html")
def form_requirements(form):
    context = {}
    for bound_field in form:
        bound_field.field.widget.attrs['class'] = 'form-control'
        if isinstance(bound_field.field, (DateField, DateTimeField)):
            context['datetimepicker'] = True
            if isinstance(bound_field.field, DateField):
                bound_field.field.datepicker = True
            else:
                bound_field.field.datetimepicker = True
    return context


@register.inclusion_tag("_notification_message.html")
def render_message(message):
    message.tags_array = message.tags.split(" ")
    return {"message": message}
