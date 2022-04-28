# Ejercicio 3 - Escibir una funcion que encuentre el elemento menor de una lista

def numero_menor_lista(lista):
    return min(lista)

def main():
    mi_lista = [ 22, 23, 59, 4, 78 ]
    print(numero_menor_lista(mi_lista))

if __name__ == '__main__':
    main()