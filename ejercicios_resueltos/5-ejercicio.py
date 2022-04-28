# Ejercicio 5 - Escribir una funcion que indique si el usuario es mayor de edad

def usuario_menor_mayor_de_edad(edad):
    if edad < 0:
        print('Edad no valida, por favor ingrese numeros positivos!')
    elif edad >= 18:
        print('Usuario mayor de edad')
    else:
        print('Usuario menor de edad')


def main():
    edad = int(input('Ingresa tu edad: '))
    usuario_menor_mayor_de_edad(edad)


if __name__ == '__main__':
    main()