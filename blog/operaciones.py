"""
    Pre entrega 5
    Se dividen las responsabilidades en archivos separados.
"""
# Recorre la lista de post, muestra el titulo y nombre del autor.
def listar_posts(lista):
    if not lista:
        print("No hay posts para mostrar.")
        return
    
    print("\n") # \n hace saltos de linea.
    print("Listado de posts")
    for post in lista: 
        titulo = post.get("titulo", "Sin titulo")   # get(clave a buscar, valor por defecto)
        autor_dict = post.get("autor")
        
        if isinstance(autor_dict, dict): # Verificamos que el autor sea un diccionario para extraer el nombre.
            nombre_autor = autor_dict.get("nombre", "Autor desconocido")
        else:
            nombre_autor = "Autor no válido"
    
        print(f"Titulo: {titulo} Autor: {nombre_autor}")


# Busca y muestra posts cuyo titulo contenga el termino
def buscar_por_titulo(lista, termino):
    if not termino.strip():
        print("La busqueda no puede estar vacia.")
        
    
    termino_minusculas = termino.lower()
    resultados = []
    
    for post in lista:
        titulo = post.get("titulo", "")
        if termino_minusculas in titulo.lower():
            resultados.append(post)
            
    
    if resultados:
        print(f"Resultados para la busqueda '{termino}': ")
        listar_posts(resultados)
    else:
        print(f"No se encontraron posts que contengan '{termino}' ")
        

# Filtra y muestra posts que contengan un tag especifico
def filtrar_por_tag(lista, tag):
    if not tag.strip():
        print("El tag de busqueda no puede estar vacio.")
        return
    
    tag_minusculas = tag.lower()
    resultados = []
    
    for post in lista:
        tags = post.get("tags", [])
        if isinstance(tags, list):
            tags_lower = [t.lower() for t in tags]
            if tag_minusculas in tags_lower:
                resultados.append(post)

    if resultados:
        print(f"Posts con el tag '{tag}':")
        listar_posts(resultados)
    else:
        print(f"No se encontraron posts con el tag '{tag}'.")