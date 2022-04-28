# Ejercicio 9 - Escribir una funcion que recibe nombre y apellido y los vaya agregando a un archivo

def pedir_nombre_completo(nombre_completo):
    with open('./archivo/nombres.txt', 'a', encoding='utf-8') as f:
        f.write(nombre_completo)
        f.write('\n')
    
    print('Nombre agregado!!')


def main():
    print('Ingrese "s" para salir')
    nombre_completo = input("Ingrese su primer nombre y primer apellido: ")
    while nombre_completo != 's':
        if nombre_completo == 's':
            break
        pedir_nombre_completo(nombre_completo)
        nombre_completo = input("Ingrese su primer nombre y primer apellido: ")
        
    


if __name__ == '__main__':
    main()