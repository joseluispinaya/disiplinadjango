from django.core.exceptions import ValidationError
import re

def validar_par(value):
    if value % 2 != 0:
        raise ValidationError("%(value)s no es un numero par", params={"value": value})
    
def validar_mayor_a_cero(value):
    if value <= 0:
        raise ValidationError("El valor de puntos debe ser mayor a cero.")
    
def validar_cel(value):
    if not re.fullmatch(r'\d{1,10}', value):
        raise ValidationError(
            "%(value)s no es válido. El celular debe ser numeros y tener como máximo 10 numeros.",
            params={"value": value}
        )