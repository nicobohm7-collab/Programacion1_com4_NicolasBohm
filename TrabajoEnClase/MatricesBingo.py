import random

print("Bienvenido al Bingo\n")
numeros = random.sample(range(1, 51), 25)
carton = [numeros[i:i+5] for i in range(0, 25, 5)]
print("Tu cartón es:")
for fila in carton:
    print(fila)
print()
numeros_sorteados = list(range(1, 51))
random.shuffle(numeros_sorteados)

for numero in numeros_sorteados:
    print(f"Se sortea el número... {numero}")
    encontrado = False

    for i in range(5):
        for j in range(5):
            if carton[i][j] == numero:
                carton[i][j] = 0
                encontrado = True

    if encontrado:
        print(" -> ¡Lo tenés!")
    else:
        print(" -> No está en tu cartón.")

    for fila in carton:
        print(fila)
    print()

    for fila in carton:
        if all(num == 0 for num in fila):
            print("¡Línea!\n")

    todo_ceros = True
    for fila in carton:
        for num in fila:
            if num != 0:
                todo_ceros = False
                break

    if todo_ceros:
        print("¡Bingo! Tu cartón quedó en:")
        for fila in carton:
            print(fila)
        break