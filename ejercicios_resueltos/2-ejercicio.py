# Ejercicio 2 - Ingresar nombre y apellido e imprimirlo al reves

def nombre_reves(nombre, apellido):
    nombre_completo = f'{nombre} {apellido}'
    return nombre_completo[::-1]


def main():
    nombre = input('Ingresa tu nombre: ')
    apellido = input('Ingresa tu apellido: ')

    print(nombre_reves(nombre, apellido))
    

if __name__ == '__main__':
    main()