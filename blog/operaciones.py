"""
    Pre entrega 5
    Se dividen las responsabilidades en archivos separados.
"""

def listar_posts(lista):
    if not lista:
        print("No hay posts para mostrar.")
        return
    
    print("\nListado de posts")
    for post in lista: 
        titulo = post.get("titulo", "Sin titulo")
        autor_dict = post.get("autor")
        
        if isinstance(autor_dict, dict):
            nombre_autor = autor_dict.get("nombre", "Autor desconocido")
        else:
            nombre_autor = "Autor no válido"
    
        print(f"Titulo: {titulo} Autor: {nombre_autor}")

def buscar_por_titulo(lista, termino):
    # Retorna None si está vacío para manejar el error en main.py
    if not termino.strip():
        return None
    
    termino_minusculas = termino.lower()
    resultados = []
    
    for post in lista:
        titulo = post.get("titulo", "")
        if termino_minusculas in titulo.lower():
            resultados.append(post)
            
    # Solo retorna los datos, sin imprimir ni formatear
    return resultados
        
def filtrar_por_tag(lista, tag):
    if not tag.strip():
        return None
    
    tag_minusculas = tag.lower()
    resultados = []
    
    for post in lista:
        tags = post.get("tags", [])
        if isinstance(tags, list):
            tags_lower = [t.lower() for t in tags]
            if tag_minusculas in tags_lower:
                resultados.append(post)

    # Solo retorna los datos
    return resultados