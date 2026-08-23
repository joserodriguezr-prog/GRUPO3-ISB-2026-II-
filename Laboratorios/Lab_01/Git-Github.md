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

# Resumen
En este primer laboratoriose se vieron los conceptos básicos de Git, GitHub y su importancia en trabajos colaborativos en ingeniería.

Lo primero fue instalar y configurar el Git, crear un repositorio local y utilizar comandos como `git add`, `git commit` y `git push`.

Además se vieron los  módulos, que son el Working Directory, Staging Area, Local Repository y Remote Repository.

Seguido a esto, se vio cómo trabajar con Git desde VSCode y cómo sincronizarlo con nuestro proyecto en GitHub.

Finalmente, se vio un poco del código de markdwon para poder presentar nuestros avances de proyecto.


