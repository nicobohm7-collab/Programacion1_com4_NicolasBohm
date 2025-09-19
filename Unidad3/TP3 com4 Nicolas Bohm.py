#Ejercicio1
edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

#Ejercicio2
nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio3
n = int(input("Ingrese un número: "))

if n % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio4
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#Ejercicio5
contraseña = input("Ingrese una contraseña: ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio6
from statistics import mean, median, mode
import random

mi_lista = [random.randint(1, 100) for _ in range(50)]

print("Lista de números:", mi_lista)

media = mean(mi_lista)
mediana = median(mi_lista)
moda = mode(mi_lista)

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana and mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana and mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana and mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar con este criterio")

#Ejercicio7
texto = input("Ingrese una frase o palabra: ")

if texto[-1].lower() in "aeiouáéíóú":
    texto = texto + "!"

print(texto)

#Ejercicio8
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese opción (1: MAYUS, 2: minus, 3: Primera mayúscula): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.capitalize())
else:
    print("Opción inválida")

#Ejercicio9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")

#Ejercicio10
hemisferio = input("En qué hemisferio está? (N/S): ").upper()
mes = int(input("Mes (1-12): "))
dia = int(input("Día (1-31): "))

if hemisferio == "N": 
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        print("Verano")
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
        print("Otoño")

elif hemisferio == "S": 
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        print("Verano")
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
        print("Primavera")
else:
    print("Hemisferio inválido")
