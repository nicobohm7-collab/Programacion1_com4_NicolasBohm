#Ejercicio1
lista_multiplos = list(range(4, 101, 4))
print(lista_multiplos)

#Ejercicio2
lista = ["pizza", "helado", "guitarra", "mate", "python"]
print(lista[3]) 

#Ejercicio3
lista_vacia = []

lista_vacia.append("hola")
lista_vacia.append("mundo")
lista_vacia.append("python")

print(lista_vacia)

#Ejercicio4
animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"

print(animales)

#Ejercicio5
#El código de este ejercicio crea una lista con numeros, luego busca el numero mas grande entre ellos y lo elimina para luego mostrar en pantalla la lista sin el.

#Ejercicio6
lista = list(range(10, 31, 5))

print(lista[0], lista[1])

#Ejercicio7
autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "fiesta"
autos[2] = "cronos"

print(autos)

#Ejercicio8
dobles = []

dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

print(dobles)

#Ejercicio9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")

compras[1][1] = "tallarines"

compras[0].remove("pan")

print(compras)

#Ejercicio10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)