from django import template


register = template.Library()


@register.filter
def translatedstatus(value: str) -> str:
    en_to_ru_statuses_map = {
        'in_progress': 'В процессе',
        'done': 'Выполнено',
        'todo': 'К выполнению',
    }
    return en_to_ru_statuses_map.get(value, value)
