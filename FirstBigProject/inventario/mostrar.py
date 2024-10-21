from utils.cargar_guardar import cargar_inventario


def mostrar_inventario(archivo):
    """Muestra en pantalla todos los productos disponibles en el inventario."""
    inventario = cargar_inventario(archivo)

    if not inventario:
        print("El inventario está vacío.")
        return

    print("Inventario disponible:")
    print("-" * 40)
    for producto, detalles in inventario.items():
        print(f"Producto: {producto}")
        print(f"  Cantidad: {detalles['cantidad']}")
        print(f"  Precio: {detalles['precio']}")
        print("-" * 40)
