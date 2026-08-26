# CONFIGURACIÓN INICIAL
    - git --version                            # Verificar instalación
    - git config --global user.name "TuNombre" # Configurar nombre de usuario
    - git config --global user.email "tu@email.com" # Configurar correo

# 4 ÁREAS DE GIT
    - Working Directory: Tu carpeta local donde editas archivos.
    - Staging Area: Zona temporal previa al guardado (git add). # Comando a usar
    - Local Repository: Tu copia local con el historial guardado (git commit). # Comando a usar
    - Remote Repository: El repositorio compartido en la nube/GitHub (git push / git clone). # Comando a usar

# TERMINAL
    - mkdir mi-repo && cd mi-repo              # Crear carpeta e ingresar a ella
    - git init                                 # Inicializar repositorio local
    - git add README.md                        # Agregar un archivo específico a Staging
    - git add .                                # Agregar todos los cambios a Staging
    - git commit -m "Initial commit"           # Guardar instantánea en el repositorio local

# VS CODE 
    - Publicar por primera vez: Control de Fuente (Sidebar) -> Publish Branch (sincroniza con GitHub).
    - En adelante, usar Commit y luego Push (Sync Changes)
    - Seleccionar Push to para conectarse a los repositorios locales
    - Añadir "remote" de GitHub 
    - Conectarse con GitHub y añadir repositorio

# Codigos

| Código / Sintaxis | Qué hace / Información | Resultado en Vista Previa |
| :--- | :--- | :--- |
| `# Título 1`<br>`## Título 2`<br>`### Título 3` | **Encabezados:** Crea títulos. A mayor cantidad de `#`, más pequeño es el nivel del título (hasta 6). | Títulos estructurados |
| `**Texto**` o `__Texto__` | **Negrita:** Resalta el texto con formato de negrita para dar énfasis. | **Texto** |
| `*Texto*` o `_Texto_` | **Cursiva:** Cambia el texto a itálica. | *Texto* |
| `***Texto***` | **Negrita y Cursiva:** Combina ambos estilos a la vez. | ***Texto*** |
| `> Esto es un texto` | **Cita en bloque:** Crea un bloque resaltado, ideal para notas, advertencias o citas externas. | Blockquote |
| `- Elemento 1`<br>`- Elemento 2` | **Lista desordenada:** Crea una lista con viñetas. (También funcionan los símbolos `*` o `+`). | Lista con puntos |
| `1. Paso uno`<br>`2. Paso dos` | **Lista ordenada:** Crea una secuencia numerada automáticamente. | Lista con números |
| `[Texto del enlace](https://...)` | **Hipervínculo:** Inserta un enlace clicable. El texto visible va en `[]` y la URL en `()`. | [Texto del enlace](URL) |
| `![Descripción](ruta_imagen.jpg)`| **Imagen:** Inserta una foto. Es igual a la sintaxis del enlace, pero con un `!` al inicio. | Muestra la imagen |
| `` `código en línea` `` | **Código Inline:** Resalta un texto breve como código dentro de un párrafo normal (usando *backticks*). | `código en línea` |
| ` ```python `<br>`print("Hola")`<br>` ``` ` | **Bloque de código:** Crea una caja de código. Si pones el nombre del lenguaje (ej: python, c), VS Code colorea la sintaxis. | Bloque de código coloreado |
| `---` o `***` | **Línea divisoria:** Dibuja una línea horizontal para separar secciones del documento. | Línea horizontal |
| `- [x] Tarea lista`<br>`- [ ] Tarea pendiente` | **Checklist:** Crea una lista de tareas interactivas. La `x` marca la casilla como completada. | Casillas de verificación |
| <code>\| Col 1 \| Col 2 \|<br>\| :--- \| :--- \|<br>\| Dato \| Dato \|</code> | **Tablas:** Crea una tabla. Los `\|` separan columnas y los `:---` definen la alineación. | Tabla estructurada |


# Resumen
En este primer laboratoriose se vieron los conceptos básicos de Git, GitHub y su importancia en trabajos colaborativos en ingeniería.

Lo primero fue instalar y configurar el Git, crear un repositorio local y utilizar comandos como `git add`, `git commit` y `git push`.

Además se vieron los  módulos, que son el Working Directory, Staging Area, Local Repository y Remote Repository.

Seguido a esto, se vio cómo trabajar con Git desde VSCode y cómo sincronizarlo con nuestro proyecto en GitHub.

Finalmente, se vio un poco del código de markdwon para poder presentar nuestros avances de proyecto.


