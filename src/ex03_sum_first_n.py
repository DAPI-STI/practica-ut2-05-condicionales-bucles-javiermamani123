"""
Ejercicio 3:
Suma de los primeros n números.
"""

def sum_first_n(n: int) -> int:
    """
    Devuelve la suma 1 + 2 + ... + n.

    - Si n <= 0, devuelve 0.
    - Debe resolverse usando un bucle (for o while).
    """
    raise NotImplementedError("Implementa sum_first_n(n)")

def sum_first_n(n: int) -> int:
    """
    Devuelve la suma 1 + 2 + ... + n.

    - Si n <= 0, devuelve 0.
    - Debe resolverse usando un bucle for o mientras.
    """
    if n <= 0:
        return 0

    total = 0
    for i in range(1, n + 1):
        total += i

    return total

# Pruebas
print(sum_first_n(5))   # 1+2+3+4+5 = 15
print(sum_first_n(10))  # 55
print(sum_first_n(0))   # 0
print(sum_first_n(-3))  # 0
