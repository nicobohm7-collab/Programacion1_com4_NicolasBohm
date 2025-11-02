def crear_archivo_inicial():
    try:
        with open("productos.txt", "x") as archivo:
            archivo.writelines([
                "Lapicera,120.5,30\n",
                "Cuaderno,350.0,15\n",
                "Regla,80.0,50\n"
            ])
            print("Archivo 'productos.txt' creado con productos iniciales.\n")
    except FileExistsError:
        pass


def leer_productos():
    productos = []
    try:
        with open("productos.txt", "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                nombre, precio, cantidad = linea.strip().split(",")
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })
                print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
    except FileNotFoundError:
        print("El archivo 'productos.txt' no existe.")
    return productos


def agregar_producto():
    nombre = input("\nIngrese el nombre del nuevo producto: ").strip()
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    print(f"\nProducto '{nombre}' agregado correctamente.\n")


def buscar_producto(productos):
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip().lower()
    encontrado = False
    for prod in productos:
        if prod["nombre"].lower() == nombre_buscar:
            print(f"\nProducto encontrado: {prod['nombre']} | Precio: ${prod['precio']} | Cantidad: {prod['cantidad']}")
            encontrado = True
            break
    if not encontrado:
        print("\nProducto no encontrado.")


def guardar_productos(productos):
    with open("productos.txt", "w") as archivo:
        for p in productos:
            archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print("\nProductos actualizados y guardados en 'productos.txt'.\n")


def main():
    crear_archivo_inicial()
    productos = leer_productos()

    print("\nOpciones:")
    print("1. Agregar nuevo producto")
    print("2. Buscar producto")
    print("3. Guardar y salir")

    opcion = input("\nSeleccione una opción (1/2/3): ").strip()

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        buscar_producto(productos)
    elif opcion == "3":
        guardar_productos(productos)
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main()
