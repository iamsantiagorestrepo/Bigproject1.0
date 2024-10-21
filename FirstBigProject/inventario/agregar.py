from utils.cargar_guardar import cargar_inventario, guardar_inventario


def agregar_producto(archivo):
    """Permite al usuario agregar un producto al inventario y lo guarda en el archivo JSON."""
    inventario = cargar_inventario(archivo)

    # Pedir al usuario los datos del producto
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input(f"Ingrese la cantidad de {nombre}: "))
    precio = float(input(f"Ingrese el precio de {nombre}: "))

    # Verificar si el producto ya existe
    if nombre in inventario:
        print(f"El producto '{nombre}' ya existe en el inventario. Actualizando cantidad y precio.")
        inventario[nombre]['cantidad'] += cantidad
        inventario[nombre]['precio'] = precio  # Actualiza el precio al último ingresado
    else:
        # Si no existe, agregar el nuevo producto
        inventario[nombre] = {'cantidad': cantidad, 'precio': precio}

    # Guardar el inventario actualizado
    guardar_inventario(archivo, inventario)