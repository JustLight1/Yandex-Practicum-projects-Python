from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_year(value):
    """Функция проверки корректности указанного года."""
    if value > timezone.now().year:
        raise ValidationError(f'Год {value} больше текущего.')
