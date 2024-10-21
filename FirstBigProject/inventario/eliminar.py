from utils.cargar_guardar import cargar_inventario, guardar_inventario


def eliminar_producto(archivo):
    """Permite al usuario eliminar un producto del inventario."""
    inventario = cargar_inventario(archivo)

    # Mostrar los productos existentes
    if not inventario:
        print("El inventario está vacío.")
        return

    print("Productos en el inventario:")
    for producto in inventario:
        print(f"- {producto} (Cantidad: {inventario[producto]['cantidad']}, Precio: {inventario[producto]['precio']})")

    # Pedir al usuario que seleccione un producto para eliminar
    nombre = input("Ingrese el nombre del producto que desea eliminar: ")

    if nombre in inventario:
        confirmar = input(f"¿Está seguro de que desea eliminar '{nombre}' del inventario? (s/n): ").lower()
        if confirmar == 's':
            del inventario[nombre]  # Eliminar el producto del inventario
            guardar_inventario(archivo, inventario)
            print(f"Producto '{nombre}' eliminado exitosamente.")
        else:
            print("Operación cancelada.")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")
