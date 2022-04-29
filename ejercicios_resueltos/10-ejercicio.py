# Ejercicio 10 - Escribir una funcion que recibe una palabra y comprueba si es un palindromo

def es_palindromo(palabra):
    palabra = palabra.replace(' ', '').lower()
    if palabra == palabra[::-1]:
        return True
    else:
        return False

def main():
    print('--- COMPRUEBA SI UNA PALABRA ES UN PALINDROMO ---')
    palabra = input('Ingresa una palabra: ')
    print(es_palindromo(palabra))


if __name__ == '__main__':
    main()