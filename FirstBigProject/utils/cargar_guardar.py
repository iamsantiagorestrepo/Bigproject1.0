import json


def cargar_inventario(archivo):
    """Carga el inventario desde un archivo JSON y lo almacena en un diccionario."""
    try:
        with open(archivo, 'r') as file:
            inventario = json.load(file)
        print("Inventario cargado exitosamente.")
        return inventario
    except FileNotFoundError:
        print(f"El archivo {archivo} no fue encontrado. Se creará uno nuevo.")
        return {}
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
        return {}


def guardar_inventario(archivo, inventario):
    """Guarda el inventario en un archivo JSON."""
    try:
        with open(archivo, 'w') as file:
            json.dump(inventario, file, indent=4)
        print("Inventario guardado exitosamente.")
    except Exception as e:
        print(f"Error al guardar el inventario: {e}")