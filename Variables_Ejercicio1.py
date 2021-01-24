#Sebastian Garcia, 19683
#Jose Pablo Ponce, 19092
#6/2/2019
#Variables_ejercicio1
#Un programa para llevar el calculo de los aportes para el regalo de la abuelita.


#Pedido de valores
print('Ingrese Nombres: ')
nombre1 = input('Ingrese Nombre 1: ')
nombre2 = input('Ingrese Nombre 2: ')
nombre3 = input('Ingrese Nombre 3: ')
nombre4 = input('Ingrese Nombre 4: ')
nombre5 = input('Ingrese Nombre 5: ')
print()
print('Ingrese Cantidades: ')
cantidad1 = input('Ingrese cantidad 1: ')
cantidad2 = input('Ingrese cantidad 2: ')
cantidad3 = input('Ingrese cantidad 3: ')
cantidad4 = input('Ingrese cantidad 4: ')
cantidad5 = input('Ingrese cantidad 5: ')
print('Ingrese Cambio de dolar a quetzal actual: ')
cambio = input('Ingrese cambio: ')
#Cambio de string a numeros
cambio = float(cambio)
cantidad1 = float(cantidad1)
cantidad2 = float(cantidad2)
cantidad3 = float(cantidad3)
cantidad4 = float(cantidad4)
cantidad5 = float(cantidad5)
#variable de cambio
conversion = cambio * 90
#Print nombres, cantidades, vuelto, total.
print('Nombre:', nombre1, ',Aporte:', cantidad1)
print('Nombre:', nombre2, ',Aporte:', cantidad2)
print('Nombre:', nombre3, ',Aporte:', cantidad3)
print('Nombre:', nombre4, ',Aporte:', cantidad4)
print('Nombre:', nombre5, ',Aporte:', cantidad5)
Total = cantidad1 + cantidad2 + cantidad3 + cantidad4 + cantidad5
Vuelto = Total - conversion
print('Total recolectado: Q.', Total)
print('Costo de amazon Echo en Quetzales: Q.', conversion)
print('Sobrante o faltante: Q.', Vuelto)
