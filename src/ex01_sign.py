"""
Ejercicio 1:
Clasifica un número como positivo, negativo o cero.
"""

def sign(n: int) -> str:
    """
    Devuelve:
    - "positivo" si n > 0
    - "negativo" si n < 0
    - "cero" si n == 0
    """
    raise NotImplementedError("Implementa sign(n)")

def sign(n: int) -> str:
    """
    Devuelve:
    - "positivo" si n > 0
    - "negativo" si n < 0
    - "cero" si n == 0
    """
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "cero"

# Pruebas del codigo
print(sign(10))   # positivo
print(sign(-5))   # negativo
print(sign(0))    # cero
