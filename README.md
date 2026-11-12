# Pre entrega 5 de Python.

Continuamos con el blog, pero en este módulo separamos el código en archivos para aplicar principios de modularización.

## Estructura del Proyecto y Responsabilidades

*   **`main.py`**: Es el archivo principal que orquesta la ejecución del programa. Importa las funciones de los demás módulos y maneja el flujo principal del menú y las salidas por pantalla.
*   **`blog/__init__.py`**: Archivo de inicialización que permite a Python reconocer el directorio `blog/` como un paquete.
*   **`blog/datos.py`**: Contiene las estructuras de datos base (diccionarios, listas y tuplas) que simulan la base de datos del blog, incluyendo los perfiles de autor y los posts.
*   **`blog/menu.py`**: Centraliza toda la interacción directa con el usuario, encargándose de mostrar las opciones, capturar los ingresos por teclado y manejar errores de tipeo.
*   **`blog/operaciones.py`**: Aísla la lógica de negocio. Contiene funciones que reciben datos, los procesan (como buscar por título o filtrar por tag) y retornan los resultados procesados sin encargarse de la impresión.
*   **`blog/validaciones.py`**: Almacena las reglas estrictas de formato. Verifica que cada post cumpla con la estructura de diccionario requerida y no contenga campos vacíos.

## Ejecución en Windows
python main.py

## Ejecución en Mac / Linux
python3 main.py