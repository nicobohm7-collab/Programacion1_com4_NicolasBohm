#Ejercicio1
for i in range(0, 101):
    print(i)

#Ejercicio2
n = int(input("Ingrese un número entero: "))
contador = 0

if n == 0:
    contador = 1
else:
    while n != 0:
        n = n // 10
        contador = contador + 1

print("Cantidad de dígitos:", contador)

#Ejercicio3
a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))

if a > b:
    a, b = b, a   

suma = 0
for i in range(a+1, b):
    suma = suma + i

print("La suma es:", suma)

#Ejercicio4
suma = 0
n = int(input("Ingrese un número (0 para terminar): "))

while n != 0:
    suma = suma + n
    n = int(input("Ingrese un número (0 para terminar): "))

print("Total acumulado:", suma)

#Ejercicio5
import random
numero = random.randint(0, 9)

intentos = 0
adivino = False

while not adivino:
    x = int(input("Adivine el número entre 0 y 9: "))
    intentos = intentos + 1
    if x == numero:
        adivino = True

print("¡Correcto! El número era", numero)
print("Cantidad de intentos:", intentos)

#Ejercicio6
for i in range(100, -1, -2):
    print(i)

#Ejercicio7
n = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(0, n+1):
    suma = suma + i

print("La suma es:", suma)

#Ejercicio8
cantidad = 100   
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad):
    n = int(input("Ingrese un número: "))
    if n % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    if n > 0:
        positivos = positivos + 1
    elif n < 0:
        negativos = negativos + 1

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

#Ejercicio9
cantidad = 100   
suma = 0

for i in range(cantidad):
    n = int(input("Ingrese un número: "))
    suma = suma + n

media = suma / cantidad
print("La media es:", media)

#Ejercicio10
n = int(input("Ingrese un número: "))
invertido = 0

while n != 0:
    resto = n % 10
    invertido = invertido * 10 + resto
    n = n // 10

print("Número invertido:", invertido)