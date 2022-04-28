# Ejercicio 6 - Escribir una funcion que indique  si un numero es par o impar

def num_par_impar(num):
    if num % 2 == 0:
        print('El numero es par')
    else:
        print('El numero es impar')

def main():
    num = int(input('Ingrese un numero: '))
    num_par_impar(num)


if __name__ == '__main__':
    main()