#Ejercicio1
def imprimir_hola_mundo():
    print("Hola Mundo!")


#Ejercicio2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"


#Ejercicio3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


#Ejercicio4
def calcular_area_circulo(radio):
    area = 3.1416 * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.1416 * radio
    return perimetro


#Ejercicio5
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas


#Ejercicio6
def tabla_multiplicar(numero):
    print(f"Tabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


#Ejercicio7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)


#Ejercicio8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


#Ejercicio9
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


#Ejercicio10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio


# PROGRAMA PRINCIPAL

#Ejercicio1
imprimir_hola_mundo()

#Ejercicio2
nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))

#Ejercicio3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio4
radio = float(input("Ingrese el radio del círculo: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

#Ejercicio5
segundos = int(input("Ingrese una cantidad de segundos: "))
print(f"Equivale a {segundos_a_horas(segundos):.2f} horas.")

#Ejercicio6
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

#Ejercicio7
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

#Ejercicio8
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"Su IMC es: {calcular_imc(peso, altura):.2f}")

#Ejercicio9
celsius = float(input("Ingrese la temperatura en °C: "))
print(f"Equivale a {celsius_a_fahrenheit(celsius):.2f} °F")

#Ejercicio10
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
print(f"El promedio es: {calcular_promedio(a, b, c):.2f}")
