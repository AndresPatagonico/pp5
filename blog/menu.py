"""
    Pre entrega 5
    Se dividen las responsabilidades en archivos separados.
"""

# Muestra el menu.
def mostrar_menu():
    print("\n<--- MENÚ DEL BLOG --->")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")
    print("-----------------------")
    
    try:
        opcion = int(input("Seleccione una opción (1 a 5): ")) # int = convierte lo ingresado en un entero.
        return opcion
    except ValueError: # Maneja el error si el usuario ingresa un valor no esperado.
        print("Opción no válida. Por favor, ingrese un número entre 1 y 5.")
        return None