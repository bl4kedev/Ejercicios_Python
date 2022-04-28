# Ejercicio 7 - Escribir una funcion que indique cuantas vocales tiene una palabra

def cuantas_vocales(palabra):
    contador = 0
    palabra = palabra.lower()
    for c in palabra:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            contador += 1
    
    print(f'El numero de vocales es: {contador}')

def main():
    string = 'murcielago'
    cuantas_vocales(string)

if __name__ == '__main__':
    main()