#EJERCICIO1
print("Hola Mundo!")

#EJERCICIO2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#EJERCICIO3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_de_residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}.")

#EJERCICIO4
import math

radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * (radio)**2
perimetro = 2 * math.pi * radio
print(f"El área del círculo es de {area} y el perímetro es de {perimetro}.")

#EJERCICIO5
cantidad_segundos = float(input("Ingrese la cantidad de segundos a convertir: "))
cantidad_horas = round(cantidad_segundos / 3600, 2)
print(f"{cantidad_segundos} segundos equivalen a {cantidad_horas} horas.")

#EJERCICIO6
numero_usuario = int(input("Ingrese un número entero: "))
multiplicacion0 = numero_usuario * 0
multiplicacion1 = numero_usuario * 1
multiplicacion2 = numero_usuario * 2
multiplicacion3 = numero_usuario * 3
multiplicacion4 = numero_usuario * 4
multiplicacion5 = numero_usuario * 5
multiplicacion6 = numero_usuario * 6
multiplicacion7 = numero_usuario * 7
multiplicacion8 = numero_usuario * 8
multiplicacion9 = numero_usuario * 9

print(f"""
  {numero_usuario} x 0 = {multiplicacion0}
  {numero_usuario} x 1 = {multiplicacion1}
  {numero_usuario} x 2 = {multiplicacion2}
  {numero_usuario} x 3 = {multiplicacion3}
  {numero_usuario} x 4 = {multiplicacion4}
  {numero_usuario} x 5 = {multiplicacion5}
  {numero_usuario} x 6 = {multiplicacion6}
  {numero_usuario} x 7 = {multiplicacion7}
  {numero_usuario} x 8 = {multiplicacion8}
  {numero_usuario} x 9 = {multiplicacion9}
      """)

#EJERCICIO7
numero_a = float(input("Ingrese un número distinto de 0: "))
numero_b = float(input("Ingrese otro número distinto de 0: "))
suma_doble = numero_a + numero_b
division_doble = round(numero_a / numero_b, 2)
multiplicacion_doble = numero_a * numero_b
resta_doble = numero_a - numero_b

print(f"""
  La suma de ambos es: {suma_doble}
  La división del primero por el segundo es: {division_doble}
  La multiplicación de ambos es: {multiplicacion_doble}
  El primero restado por el segundo es: {resta_doble}
      """)

#EJERCICIO08
peso = float(input("Ingrese su peso en kgs: "))
altura = float(input("Ingrese su altura en mts: "))
imc = round(peso / altura**2, 2)
print(f"Su IMC es de: {imc}.")

#EJERCICIO09
grados_celsius = float(input("Por favor, una temperatura en °C: "))
grados_fahrenheit = round((9/5)*grados_celsius+32, 2)
print(f"{grados_celsius} °C son equivalentes a {grados_fahrenheit} °F.")

#EJERCICIO10
numero_d = float(input("Por favor, ingrese el primer número: "))
numero_e = float(input("Por favor, ingrese el segundo número: "))
numero_f = float(input("Por favor, ingrese el tercer número: "))
suma_triple = numero_d + numero_e + numero_f
promedio_triple = round(suma_triple/3, 2)
print(f"El promedio de los números ingresados es {promedio_triple}.")