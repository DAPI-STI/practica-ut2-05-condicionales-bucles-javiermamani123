"""
Ejercicio 2:
Determina si un año es bisiesto (reglas típicas).
"""

def is_leap_year(year: int) -> bool:
    """
    Devuelve True si el año es bisiesto, False en caso contrario.

    Reglas:
    - Un año es bisiesto si es divisible por 4
    - Excepto si es divisible por 100
    - Pero sí es bisiesto si es divisible por 400
    """
    raise NotImplementedError("Implementa is_leap_year(year)")


def is_leap_year(year: int) -> bool:
    """
    Devuelve True si el año es bisiesto, False en caso contrario.

    Reglas:
    - Un año es bisiesto si es divisible por 4
    - Excepto si es divisible por 100
    - Pero sí es bisiesto si es divisible por 400
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# Pruebas
print(is_leap_year(2020))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2000))  # True
print(is_leap_year(2023))  # False
