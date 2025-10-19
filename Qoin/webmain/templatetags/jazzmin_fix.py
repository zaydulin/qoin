from django import template

register = template.Library()

@register.filter
def length_is(value, arg):
    """
    Фильтр для Jazzmin совместимости
    Проверяет, равна ли длина значения указанному числу
    """
    try:
        return len(value) == int(arg)
    except (TypeError, ValueError):
        return False