"""
    Pre entrega 5
    Se dividen las responsabilidades en archivos separados.
"""
from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post

if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            listar_posts(posts)

        elif opcion == 2:
            termino = input("Ingrese el título o palabra a buscar: ")
            buscar_por_titulo(posts, termino)

        elif opcion == 3:
            tag_buscado = input("Ingrese el tag a filtrar: ")
            filtrar_por_tag(posts, tag_buscado)

        elif opcion == 4:
            print("--- VALIDACIÓN DE POSTS ---")
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