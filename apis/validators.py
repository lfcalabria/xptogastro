from django.utils import timezone
from rest_framework.exceptions import ValidationError


def validate_not_in_future(value):
    if value > timezone.now().date():
        raise ValidationError('A data não pode estar no futuro.')


def validate_not_zero(value):
    if value <= 0.:
        raise ValidationError('O valar deve ser positivo e maior que zero.')
