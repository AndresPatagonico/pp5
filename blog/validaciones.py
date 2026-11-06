"""
    Pre entrega 5
    Se dividen las responsabilidades en archivos separados.
"""
from .datos import estados_post

# Verifica si un post cumple con todas las reglas estructurales y de datos.
def validar_post(post):
    if not isinstance(post, dict):
        return "Error: El post no es un diccionario."

    # Claves obligatorias que deben existir
    claves_necesarias = ["id", "titulo", "contenido", "autor", "tags", "estado"]
    for clave in claves_necesarias:
        if clave not in post:
            return f"Error: Falta la clave obligatoria '{clave}'."

    # Validar que el título no esté vacío
    if not post["titulo"].strip():
        return "Error: El título no puede estar vacío."

    # Validar que el contenido no esté vacío
    if not post["contenido"].strip():
        return "Error: El contenido no puede estar vacío."

    # Validar que el autor sea un diccionario y tenga la clave "nombre"
    autor = post["autor"]
    if not isinstance(autor, dict) or "nombre" not in autor:
        return "Error: La clave 'autor' debe ser un diccionario válido con la clave 'nombre'."

    # Validar que los tags sean una lista
    if not isinstance(post["tags"], list):
        return "Error: La clave 'tags' debe ser una lista."

    # Validar que el estado pertenezca a la tupla permitida
    if post["estado"] not in estados_post:
        return f"Error: El estado '{post['estado']}' no es válido. Debe ser uno de {estados_post}."

    return True

