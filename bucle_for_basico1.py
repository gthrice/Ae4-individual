''' ejercios bucles for basicos en python hecho por Felipe Burgos para el bootcamp de Python de skillnest'''
print('\nBienvenido a el recorrido bucles basicos en python')

while True :    
    print (' Ejercicio 1. Básico \n \
Ejercicio 2. Múltiples de 2 \n \
Ejercicio 3. Contando Vanilla Ice \n \
Ejercicio 4. Wow. Número gigante a la vista \n \
Ejercicio 5. Regrésame al 3 \n \
Ejercicio 6. Contador dinámico \n')
    ejercicio = int(input('Elige un ejercicio por su numero, si quieres salir presiona 0: '))
    if ejercicio == 0:
        print('Saliendo del programa...')
        break
    elif ejercicio not in [1, 2, 3, 4, 5, 6]:
        print('Opción no válida. Por favor, elige un número entre 1 y 6 o 0 para salir.\n\n Ejercicios disponibles:')
        continue
    elif ejercicio == 1:
        print('Ejercicio 1. Básico')
        print('Intruccion: imprime todos los números enteros del 0 al 100.')
        for ej1 in range(101):
            print(ej1)
        print('Fin del bucle')
        print('Ejercicio 1 completado.\n')
        print('\n Ejercicios disponibles:')
        continue
    elif ejercicio == 2:
        print('Ejercicio 2. Múltiples de 2')
        print('Intruccion: imprime todos los números múltiplos de 2 entre 2 y 500')
        for ej2 in range(2, 501, 2):
            print(ej2)
        print('Fin del bucle')
        print('Ejercicio 2 completado.\n')
        print('\n Ejercicios disponibles:')
        continue
    elif ejercicio == 3:
        print('Ejercicio 3. Contando Vanilla Ice')
        print('Intruccion: imprime los números enteros del 1 al 100.\nSi es divisible por 5 imprime “ice ice” en vez del número.\n Si es divisible por 10, imprime “baby”')
        for ej3 in range(1, 101):
            if ej3 % 10 == 0:
                print('baby')
            elif ej3 % 5 == 0:
                print('ice ice')
            else:
                print(ej3)
        print('Fin del bucle')
        print('Ejercicio 3 completado.\n')
        print('\n Ejercicios disponibles:')
        continue
    elif ejercicio == 4:
        print('Ejercicio 4. Wow. Número gigante a la vista')
        print('Intruccion: imprime la suma de todos los números pares entre 1 y 500000')
        suma = 0
        for ej4 in range(1, 500001):
            if ej4 % 2 == 0:
                suma += ej4
        print(suma)
        print('Fin del bucle')
        print('Ejercicio 4 completado.\n')
        print('\n Ejercicios disponibles:')
        continue
    elif ejercicio == 5:
        print('Ejercicio 5. Regrésame al 3')
        print('Intruccion: imprime todos los números enteros del 2024 al 0 de 3 en 3')
        for ej5 in range(2024, 0, -3):
            print(ej5)
        print('Fin del bucle')
        print('Ejercicio 5 completado.\n')
        print('\n Ejercicios disponibles:')
        continue
    elif ejercicio == 6:
        print('\nEjercicio 6. Contador dinámico\n')
        print('Instruccion: establece tres variables: numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal,\n imprime los números enteros que sean múltiplos de multiplo.\n')
        numInicial = int(input('Introduce el número inicial: '))
        numFinal = int(input('Introduce el número final: '))
        multiplo = int(input('Introduce el múltiplo: '))
        for ej6 in range(numInicial, numFinal+1, multiplo):
            if ej6 % multiplo == 0:
                print(ej6)
            print('Fin del bucle')
        print('Ejercicio 6 completado.\n')
        print('\n Ejercicios disponibles:')
        continue