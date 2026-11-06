"""
    Pre entrega 5
    Se dividen las responsabilidades en archivos separados.
"""

# Perfil autor.
perfil_autor = {
    "nombre": "Bel Arena",
    "bio": "Desarrolladora web y creadora de contenido sobre programación.",
    "especialidad": "Python y Django",
    "redes_sociales": ["@bel_dev", "@bel_python"]
}

# Estados post.
estados_post = ("borrador", "publicado", "archivado")

# Etiquetas Blog.
etiquetas_blog = {"Python", "Django", "Web", "Backend", "Python"}

# Post.
posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "En este post veremos cómo empezar a programar con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Qué es Django",
        "contenido": "Django es un framework web creado con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Django", "Web"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con listas",
        "contenido": "Las listas permiten guardar varios elementos en una sola variable.",
        "autor": perfil_autor,
        "tags": ["Python", "Listas"],
        "estado": "archivado"
    },
        {
        "id": 4,
        "titulo": "Test",
        "contenido": "TEST - Las listas permiten guardar varios elementos en una sola variable.",
        "autor": perfil_autor,
        "tags": ["Python", "Listas","TEST"],
        "estado": "publicado"
    }
]