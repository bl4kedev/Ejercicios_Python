# Ejercicio 8 - Escribir una aplicacion que recibe una cantidad infinita de numeros hasta
# decir basta, luego que devuelva la suma de los numeros ingresados

def main():
    contador = 0
    print('Pulse 0 para salir!')
    num = int(input('Ingrese un numero: '))

    while num != 0:
        contador += num
        num = int(input('Ingrese otro numero: '))

    print('El resultado es: ', contador)


if __name__ == '__main__':
    main()