from django import template
import locale
register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return ''
    

@register.filter(name='formato_moneda')
def formato_moneda(value):
    try:
        locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')  # Ajusta la configuración regional según tus necesidades
        return locale.format_string("%d", value, grouping=True)
    except (ValueError, TypeError):
        return value