
import random

def GenerarSaldos():
    clientes = {} 
    nombres = ["Esteban", "Gustavo", "Fabian", "Anthony", "Daniela", "Berta", "Valentina", "Brandon", "Cristhoper", "Larry"]
    for nombre in nombres:
        saldo = random.randint(1000, 10000) #El random lo que genera un saldo aleatorio entre los numeros colocados
        clientes[nombre] = saldo
    return clientes


def ClasificarSaldos(clientes):
    bajo = {}  # Diccionario para saldos bajos
    medio = {}  # Diccionario para saldos medios
    alto = {}  # Diccionario para saldos altos
    for nombre, saldo in clientes.items():
        if saldo < 3000:
            bajo[nombre] = saldo
        elif saldo < 7000:
            medio[nombre] = saldo
        else:
            alto[nombre] = saldo
    return bajo, medio, alto


def calcular_estadisticas(clientes):
    saldos = list(clientes.values()) #El uso del values es para valores asociados a las claves de un diccionario
    SaldoAlto = max(saldos) #Max es para el valor mas grande 
    SaldoBajo = min(saldos) #Min para el valor mas pequeño
    SaldoPromedio = sum(saldos) / len(saldos) #Sum es para sumar valores numericos y el Len es para determinar de manera mas rapida los elementos que hay  
    MediaGeometrica = CalcularMediaGeometrica(saldos)  
    return SaldoAlto, SaldoBajo, SaldoPromedio, MediaGeometrica


def CalcularMediaGeometrica(numeros):
    producto = 1
    for num in numeros:
        producto *= num
    MediaGeometrica = producto ** (1 / len(numeros))
    return MediaGeometrica


def main():
    clientes = {} 
    
    while True: #Es un bucle infinito para mostrar el menú hasta que el usuario decida salir
        print("\nMenú de opciones:")  
        print("1. Generar saldos aleatorios para 10 clientes")
        print("2. Clasificar saldos")
        print("3. Ver estadísticas")
        print("4. Calcular media geométrica")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ") #Solicita al usuario que elija una opción
        
        if opcion == '1':
            clientes = GenerarSaldos() #Este lo que genera son los saldos para los clientes
            print("Saldos generados para 10 clientes:", clientes)  
        elif opcion == '2':
            if clientes: 
                bajo, medio, alto = ClasificarSaldos(clientes)  
                print("Saldos clasificados:")
                print("Bajo:", bajo)  
                print("Medio:", medio) 
                print("Alto:", alto)  
            else:
                print("Primero debe generar los saldos.") #Este lo que muestra es un mensaje si no hay clientes generados
        elif opcion == '3':
            if clientes:  
                SaldoAlto, SaldoBajo, SaldoPromedio, MediaGeometrica = calcular_estadisticas(clientes)  
                print("Estadísticas de saldos:")
                print("Saldo más alto:", SaldoAlto)  
                print("Saldo más bajo:", SaldoBajo) 
                print("Saldo promedio:", SaldoPromedio) 
                print("Media geométrica:", MediaGeometrica)  
            else:
                print("Primero debe generar los saldos.")  # Muestra un mensaje si no hay clientes generados
        elif opcion == '4':
            if clientes:  
                MediaGeometrica = CalcularMediaGeometrica(list(clientes.values())) #Este es el que calcula la media geométrica de los saldos
                print("Media geométrica de los saldos:", MediaGeometrica) #Aquí lo imprime y lo muestra
            else:
                print("Primero debe generar los saldos.") 
        elif opcion == '5':
            print("Gracias por usar la aplicación. ¡Hasta luego!")  
            break  #Este sirve para Salir del bucle y finaliza el programa
        else:
            print("Opción no válida. Inténtelo de nuevo.") 

if __name__ == "__main__":
    main() #Lo que hace es ejecutar la función principal 