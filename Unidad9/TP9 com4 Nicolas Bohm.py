#Ejercicio1

def factorial_recursivo(n):
    """Calcula el factorial de un número n de forma recursiva."""
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def ejecutar_ejercicio1():
    print("\n--- EJERCICIO 1: Factorial ---")
    try:
        max_num = int(input("Ingrese un número entero positivo para calcular sus factoriales: "))
        if max_num < 0:
            print("Por favor, ingrese un número no negativo.")
            return

        print(f"\nFactoriales desde 1 hasta {max_num}:")
        for i in range(1, max_num + 1):
            resultado = factorial_recursivo(i)
            print(f"{i}! = {resultado}")

    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")


#Ejercicio2

def fibonacci_recursivo(pos):
    """Calcula el valor de la serie de Fibonacci en la posición 'pos'."""
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)

def ejecutar_ejercicio2():
    print("\n--- EJERCICIO 2: Serie de Fibonacci ---")
    try:
        max_pos = int(input("Ingrese la posición máxima para la serie de Fibonacci: "))
        if max_pos < 0:
            print("Por favor, ingrese una posición no negativa.")
            return

        print(f"\nSerie de Fibonacci hasta la posición {max_pos}:")
        serie = [fibonacci_recursivo(i) for i in range(max_pos + 1)]
        print(serie)

    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")


#Ejercicio3

def potencia_recursiva(base, exponente):
    """Calcula base^exponente de forma recursiva (maneja exponentes negativos)."""
    if exponente == 0:
        return 1
    elif exponente > 0:
        return base * potencia_recursiva(base, exponente - 1)
    else: 
        return 1 / potencia_recursiva(base, -exponente)

def ejecutar_ejercicio3():
    print("\n--- EJERCICIO 3: Potencia ---")
    try:
        base = float(input("Ingrese la base (n): "))
        exponente = int(input("Ingrese el exponente (m): "))
        
        resultado = potencia_recursiva(base, exponente)
        print(f"\nEl resultado de {base}^{exponente} es: {resultado}")

    except ValueError:
        print("Entrada no válida. Asegúrese de ingresar números.")


#Ejercicio4

def decimal_a_binario_recursivo(n):
    """Convierte un número decimal positivo a binario recursivamente."""
    if n == 0:
        return ""
    
    cociente = n // 2
    resto = n % 2
    return decimal_a_binario_recursivo(cociente) + str(resto)

def ejecutar_ejercicio4():
    print("\n--- EJERCICIO 4: Decimal a Binario ---")
    try:
        num_decimal = int(input("Ingrese un número decimal positivo: "))
        if num_decimal < 0:
             print("Por favor, ingrese un número positivo.")
             return
        
        resultado = decimal_a_binario_recursivo(num_decimal)
        
        if num_decimal == 0:
            print("0 en binario es: 0")
        else:
            print(f"{num_decimal} en binario es: {resultado}")

    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")
        

#Ejercicio5

def es_palindromo(palabra):
    """Verifica si una cadena es un palíndromo de forma recursiva."""
    if len(palabra) <= 1:
        return True

    if palabra[0].lower() != palabra[-1].lower():
        return False

    else:
        return es_palindromo(palabra[1:-1])

def ejecutar_ejercicio5():
    print("\n--- EJERCICIO 5: Palíndromo ---")
    palabra = input("Ingrese una palabra (sin espacios ni tildes): ")
    es_pali = es_palindromo(palabra)
    print(f"'{palabra}' es un palíndromo: {es_pali}")


#Ejercicio6

def suma_digitos(n):
    """Calcula la suma de los dígitos de un número entero positivo recursivamente (sin convertir a string)."""
    if n == 0:
        return 0
    
    ultimo_digito = n % 10
    resto_del_numero = n // 10
    
    return ultimo_digito + suma_digitos(resto_del_numero)

def ejecutar_ejercicio6():
    print("\n--- EJERCICIO 6: Suma de Dígitos ---")
    try:
        num = int(input("Ingrese un número entero positivo: "))
        if num < 0:
             print("Por favor, ingrese un número positivo.")
             return
        
        resultado = suma_digitos(num)
        print(f"La suma de los dígitos de {num} es: {resultado}")
        
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")


#Ejercicio7

def contar_bloques(n):
    """Calcula el total de bloques necesarios para una pirámide de 'n' niveles."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    else:
        return n + contar_bloques(n - 1)

def ejecutar_ejercicio7():
    print("\n--- EJERCICIO 7: Contar Bloques de Pirámide ---")
    try:
        niveles = int(input("Ingrese el número de bloques en el nivel más bajo (niveles): "))
        if niveles < 0:
             print("El número de niveles debe ser positivo.")
             return
        
        resultado = contar_bloques(niveles)
        print(f"Total de bloques necesarios para {niveles} niveles: {resultado}")
        
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")


#Ejercicio8

def contar_digito(numero, digito):
    """Cuenta las ocurrencias de un dígito en un número de forma recursiva."""
    if numero == 0:
        return 0

    ultimo_digito = numero % 10
    
    coincide = 1 if ultimo_digito == digito else 0
    
    resto_del_numero = numero // 10
    
    return coincide + contar_digito(resto_del_numero, digito)

def ejecutar_ejercicio8():
    print("\n--- EJERCICIO 8: Contar Dígito ---")
    try:
        num = int(input("Ingrese el número entero positivo (numero): "))
        digito_str = input("Ingrese el dígito a buscar (0-9): ")
        
        if num < 0 or not digito_str.isdigit() or len(digito_str) != 1:
             print("Entrada no válida. Asegúrese de que el número sea positivo y el dígito sea uno solo.")
             return
        
        digito = int(digito_str)
        resultado = contar_digito(num, digito)
        print(f"El dígito {digito} aparece {resultado} veces en el número {num}.")
        
    except ValueError:
        print("Entrada no válida.")

#Menú

def menu_principal():
    print("\nMENÚ")
    ejecutar_ejercicio1()
    ejecutar_ejercicio2()
    ejecutar_ejercicio3()
    ejecutar_ejercicio4()
    ejecutar_ejercicio5()
    ejecutar_ejercicio6()
    ejecutar_ejercicio7()
    ejecutar_ejercicio8()
    
    print("\nFIN DEL PROGRAMA.")


menu_principal()