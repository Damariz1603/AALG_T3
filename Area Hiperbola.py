"""Área de la intersección elipse-hipérbola por el método de Montecarlo."""
import math
import random
def pedir_float(mensaje):
    while True:
        try:
            v = float(input(mensaje))
            if v > 0:
                return v
            print("  El valor debe ser mayor que 0.")
        except ValueError:
            print("  Ingrese un número válido.")
def pedir_entero(mensaje):
    while True:
        try:
            v = int(input(mensaje))
            if v > 0:
                return v
            print("  El valor debe ser mayor que 0.")
        except ValueError:
            print("  Ingrese un número entero válido.")
def en_elipse(x, y, a, b):
    return x**2 / a**2 + y**2 / b**2 <= 1
def en_hiperbola(x, y, c, d):
    return x**2 / c**2 - y**2 / d**2 >= 1
def montecarlo(a, b, c, d, n):
    dentro_elipse = 0
    interseccion = 0
    for _ in range(n):
        x = random.uniform(-a, a)   # decimal aleatorio en [-a, a]
        y = random.uniform(-b, b)   # decimal aleatorio en [-b, b]
        if en_elipse(x, y, a, b):
            dentro_elipse += 1
            if en_hiperbola(x, y, c, d):
                interseccion += 1
    return dentro_elipse, interseccion
def main():
    print("=== Montecarlo: intersección elipse - hipérbola ===")
    a = pedir_float("Ingrese a (elipse): ")
    b = pedir_float("Ingrese b (elipse): ")
    c = pedir_float("Ingrese c (hipérbola): ")
    d = pedir_float("Ingrese d (hipérbola): ")
    n = pedir_entero("Cantidad de puntos aleatorios: ")
    dentro_elipse, interseccion = montecarlo(a, b, c, d, n)
    area_elipse = math.pi * a * b
    area_inter = area_elipse * interseccion / dentro_elipse if dentro_elipse else 0.0
    print("\n--- Resultados ---")
    print(f"Puntos generados                      : {n}")
    print(f"Puntos dentro de la elipse            : {dentro_elipse}")
    print(f"Puntos en la intersección             : {interseccion}")
    print(f"Área de la elipse (π·a·b)             : {area_elipse:.4f}")
    print(f"Área aproximada de la intersección    : {area_inter:.4f}")
    print("(= área elipse × puntos intersección / puntos en elipse)")
if __name__ == "__main__":
    main()