from django.core.exceptions import ValidationError
import os


def validate_file_extension(value):
    ext=os.path.splitext(value.name)[1]
    valid_extension=[".pdf"]
    valid_size= 5*1024*1024

    if not ext.lower() in valid_extension:
        raise ValidationError("Must be a pdf file.")

    if value.size>valid_size:
        raise ValidationError("file size must be less than or equal to 5MB")

    return value


