from django.core.exceptions import ValidationError


def only_numbers(value):
    if value[0] == '+':
        value = value[1:]
    if not value.isdigit():
        raise ValidationError('This field can only contain numeric values and "+" at the beginning.')
