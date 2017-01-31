from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def script_include(context, script, **kwargs):
    if 'scripts' not in context:
        context['scripts'] = []

    include_once = 'once' in kwargs and kwargs['once']

    if (not include_once) or (include_once and script not in context['scripts']):
        context['scripts'].append(script)