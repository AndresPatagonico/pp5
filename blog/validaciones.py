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

    # Accesos seguros con .get()
    titulo = post.get("titulo", "")
    contenido = post.get("contenido", "")
    autor = post.get("autor")
    tags = post.get("tags")
    estado = post.get("estado")

    # Validar que el título no esté vacío y sea texto
    if not isinstance(titulo, str) or not titulo.strip():
        return "Error: El título no puede estar vacío y debe ser texto."

    # Validar que el contenido no esté vacío y sea texto
    if not isinstance(contenido, str) or not contenido.strip():
        return "Error: El contenido no puede estar vacío y debe ser texto."

    # Validar que el autor sea un diccionario y tenga la clave "nombre"
    if not isinstance(autor, dict) or "nombre" not in autor:
        return "Error: La clave 'autor' debe ser un diccionario válido con la clave 'nombre'."

    # Validar que los tags sean una lista
    if not isinstance(tags, list):
        return "Error: La clave 'tags' debe ser una lista."

    # Validar que el estado pertenezca a la tupla permitida
    if estado not in estados_post:
        return f"Error: El estado '{estado}' no es válido. Debe ser uno de {estados_post}."
    
    return True