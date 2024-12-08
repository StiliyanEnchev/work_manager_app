from django.core.exceptions import ValidationError

def only_numbers(value):
    if not str(value).isdigit():
        raise ValidationError('This field can only contain numeric values.')