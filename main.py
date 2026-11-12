"""
    Pre entrega 5
    Se dividen las responsabilidades en archivos separados.
"""
from blog.datos import posts
from blog.menu import mostrar_menu, pedir_termino_busqueda, pedir_tag_filtro
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post

if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            listar_posts(posts)

        elif opcion == 2:
            # El input se llama desde menu.py
            termino = pedir_termino_busqueda()
            resultados = buscar_por_titulo(posts, termino)
            
            # La lógica de impresión se maneja acá
            if resultados is None:
                print("La búsqueda no puede estar vacía.")
            elif resultados:
                print(f"\nResultados para la búsqueda '{termino}': ")
                listar_posts(resultados)
            else:
                print(f"No se encontraron posts que contengan '{termino}'.")

        elif opcion == 3:
            tag_buscado = pedir_tag_filtro()
            resultados = filtrar_por_tag(posts, tag_buscado)
            
            if resultados is None:
                print("El tag de búsqueda no puede estar vacío.")
            elif resultados:
                print(f"\nPosts con el tag '{tag_buscado}':")
                listar_posts(resultados)
            else:
                print(f"No se encontraron posts con el tag '{tag_buscado}'.")

        elif opcion == 4:
            print("\n--- VALIDACIÓN DE POSTS ---")
            for i, post in enumerate(posts, start=1):
                resultado = validar_post(post)
                if resultado is True:
                    print(f"Post {i}: Válido")
                else:
                    print(f"Post {i}: {resultado}")

        elif opcion == 5:
            print("\nGracias vuelvas prontos")
            break

        else:
            if opcion is not None:
                print("Opción no válida. Por favor, elegí un número del 1 al 5.")