from django import template

register = template.Library()


@register.inclusion_tag("main/terminal.html")
def terminal(task, user, program):
    return {"task": task, "user": user, "program": program}
