from django.core.exceptions import ValidationError
import os


def validate_file_size(value):
    max_size_mb = 10
    if value.size > max_size_mb * 1024 * 1024:  # Convierte MB a bytes
        raise ValidationError(f"El archivo no puede pesar más de {max_size_mb} MB.")

def validate_file_extension(value):
    valid_extensions = ['.pdf']
    ext = os.path.splitext(value.name)[1]
    if ext.lower() not in valid_extensions:
        raise ValidationError("Solo se permiten archivos con extensión PDF.")