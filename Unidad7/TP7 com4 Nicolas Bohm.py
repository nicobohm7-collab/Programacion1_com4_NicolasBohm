import csv
import os


# Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("# Ejercicio 1 - Frutas añadidas:")
print(precios_frutas)
print("-" * 50)


# Ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("# Ejercicio 2 - Precios actualizados:")
print(precios_frutas)
print("-" * 50)


# Ejercicio 3
lista_frutas = list(precios_frutas.keys())

print("# Ejercicio 3 - Lista de frutas (keys):")
print(lista_frutas)
print("-" * 50)



# EJERCICIO 4
print("# Ejercicio 4 - Agenda Telefónica")

contactos = {}

print("\n--- Carga de 5 Contactos ---")
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ").strip()
    numero = input(f"Ingrese el número de {nombre}: ").strip()
    contactos[nombre] = numero

nombre_buscar = input("\nIngrese el nombre del contacto a consultar: ").strip()

if nombre_buscar in contactos:
    print(f"El número de {nombre_buscar} es: {contactos[nombre_buscar]}")
else:
    print(f"El contacto '{nombre_buscar}' no existe.")
print("-" * 50)



# EJERCICIO 5
print("# Ejercicio 5 - Recuento de Palabras")

frase = input("Ingrese una frase (ej: hola mundo hola): ").lower()

palabras = frase.split()

palabras_unicas = set(palabras)
print(f"Palabras únicas: {palabras_unicas}")

recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1 
    
print(f"Recuento: {recuento}")
print("-" * 50)


# EJERCICIO 6
print("# Ejercicio 6 - Promedio de Notas de Alumnos")

alumnos_notas = {}
num_alumnos = 3

for i in range(num_alumnos):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ").strip()
    
    try:
        nota1 = float(input(f"Ingrese la nota 1 de {nombre}: "))
        nota2 = float(input(f"Ingrese la nota 2 de {nombre}: "))
        nota3 = float(input(f"Ingrese la nota 3 de {nombre}: "))
        
        alumnos_notas[nombre] = (nota1, nota2, nota3)
    except ValueError:
        print("Error: Ingrese solo números para las notas. Saltando este alumno.")

print("\n--- Resultados del Promedio ---")
for nombre, notas in alumnos_notas.items():
    if notas: 
        promedio = sum(notas) / len(notas)
        print(f"El promedio de {nombre} es: {promedio:.2f}") 
print("-" * 50)


# EJERCICIO 7
print("# Ejercicio 7 - Sets de Estudiantes")

parcial1 = {101, 103, 105, 107, 109, 111, 113, 115}
parcial2 = {101, 102, 105, 108, 111, 112, 114, 115}

print(f"Aprobados Parcial 1: {parcial1}")
print(f"Aprobados Parcial 2: {parcial2}")

ambos_aprobados = parcial1.intersection(parcial2)
print(f"\n1. Aprobaron AMBOS parciales (Intersección): {ambos_aprobados}")

solo_uno = parcial1.symmetric_difference(parcial2)
print(f"2. Aprobaron SOLO UNO (Diferencia Simétrica): {solo_uno}")

total_aprobados = parcial1.union(parcial2)
print(f"3. Total de estudiantes (Unión): {total_aprobados}")
print("-" * 50)



# EJERCICIO 8
print("# Ejercicio 8 - Gestor de Stock")

stock_productos = {"lapiz": 50, "goma": 20, "regla": 10}

while True:
    print("\n--- MENU DE STOCK ---")
    print("Stock actual:", stock_productos)
    print("1. Consultar Stock de un producto")
    print("2. Agregar/Actualizar Stock")
    print("0. Salir")
    
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        producto = input("Ingrese el nombre del producto a consultar: ").lower().strip()
        cantidad = stock_productos.get(producto)
        
        if cantidad is not None:
            print(f"Stock de {producto}: {cantidad} unidades.")
        else:
            print(f"El producto '{producto}' no está en el stock.")
        
    elif opcion == "2":
        producto = input("Ingrese el nombre del producto a actualizar: ").lower().strip()
        try:
            unidades = int(input("Ingrese la cantidad a sumar al stock: "))
        except ValueError:
            print("Cantidad inválida. Debe ser un número entero.")
            continue
            
        if producto in stock_productos:
            stock_productos[producto] += unidades
            print(f"Stock de {producto} actualizado a: {stock_productos[producto]} unidades.")
        else:
            stock_productos[producto] = unidades
            print(f"Nuevo producto '{producto}' agregado con stock: {stock_productos[producto]} unidades.")

    elif opcion == "0":
        print("Saliendo del gestor de stock.")
        break
        
    else:
        print("Opción no válida. Intente nuevamente.")
print("-" * 50)



# EJERCICIO 9
print("# Ejercicio 9 - Agenda con Tuplas")

agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("jueves", "09:30"): "Entrega de proyecto"
}

print(f"Agenda actual: {agenda}")

dia_consulta = input("\nIngrese el día a consultar (ej: lunes): ").lower().strip()
hora_consulta = input("Ingrese la hora a consultar (ej: 10:00): ").strip()

clave_consulta = (dia_consulta, hora_consulta)

evento = agenda.get(clave_consulta)

if evento:
    print(f"Actividad para el {dia_consulta} a las {hora_consulta}: {evento}")
else:
    print("No hay actividad programada para esa fecha y hora.")
print("-" * 50)



# EJERCICIO 10
print("# Ejercicio 10 - Invertir Diccionario")

original_paises = {
    "Argentina": "Buenos Aires", 
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Perú": "Lima"
}

invertido_capitales = {}

for pais, capital in original_paises.items():
    invertido_capitales[capital] = pais

print(f"Diccionario Original (País: Capital): {original_paises}")
print(f"Diccionario Invertido (Capital: País): {invertido_capitales}")
print("-" * 50)