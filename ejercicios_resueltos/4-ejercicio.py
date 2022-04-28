# Ejercicio 4 - Escribir una funcion que devuelve el volumen de una esfera por su radio
# 4/3 * pi * r ** 3

from math import pi


def volumen_esfera_radio(radio):
    volumen = round(4/3 * pi * radio ** 3, 3)
    return volumen


def main():
    radio = float(input('Ingresar la radio de la esfera: '))
    print(volumen_esfera_radio(radio))


if __name__ == '__main__':
    main()