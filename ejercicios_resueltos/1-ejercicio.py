# Ejercicio 1 - Multiplicar dos numeros sin usar el simbolo de multiplicar

def multiplicar(num_1, num_2):
    multiplicacion = 0
    for n in range(1, num_2 + 1):
        multiplicacion += num_1
    
    return multiplicacion


def main():
    print(multiplicar(10, 9))


if __name__ == '__main__':
    main()