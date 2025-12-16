"""
Ejercicio 5:
Tabla de multiplicar.
"""

def multiplication_table(n: int) -> list[int]:
    """
    Devuelve una lista con 10 elementos:
    [n*1, n*2, ..., n*10]
    """
    raise NotImplementedError("Implementa multiplication_table(n)")


def multiplication_table(n: int) -> list[int]:
    """
    Devuelve una lista con 10 elementos:
    [n*1, n*2, ..., n*10]
    """
    return [n * i for i in range(1, 11)]

# Pruebas
print(multiplication_table(3))  # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
print(multiplication_table(7))  # [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
