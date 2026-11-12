"""
    Pre entrega 5
    Se dividen las responsabilidades en archivos separados.
"""

def mostrar_menu():
    print("\n<--- MENÚ DEL BLOG --->")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")
    print("-----------------------")
    
    try:
        opcion = int(input("Seleccione una opción (1 a 5): "))
        return opcion
    except ValueError:
        print("Opción no válida. Por favor, ingrese un número entre 1 y 5.")
        return None

# Nuevas funciones para centralizar los inputs solicitadas en la corrección
def pedir_termino_busqueda():
    return input("Ingrese el título o palabra a buscar: ")

def pedir_tag_filtro():
    return input("Ingrese el tag a filtrar: ")