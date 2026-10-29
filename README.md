# API Carpincho Informática
Backend de una tienda de informática y hardware que permite carga, lectura, actualización y borrado de productos, ventas y usuarios. Otras funcionalidades incluyen un panel de administración, configuración de Docker y documentación estándar (OpenAPI Specification)

### Deploy en Render
La aplicación está desplegada a través de [render]()

### Proyecto frontend que consume la API
[Carpincho Informática Frontend]()

### Prerrequisitos
- [Python](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

### Instrucciones de instalación
1. Clonar repositorio `git clone https://github.com/Joaquin-CasVar/Carpincho-Informatica-API.git`
2. Ingresar a el directorio clonado `cd Carpincho-Informatica-API`
3. Instalar dependencias `uv sync`

### Cómo ejecutar el proyecto
1. Preparar Base de Datos `uv run src/manage.py migrate`
2. Inicializar proyecto `uv run src/manage.py runserver`

---

## Diagrama de la Base de Datos
![Diagrama de la Base de Datos](https://i.imgur.com/F9nx59g.png)

---

## Proyecto funcionando
Ruta base
![Ruta base]()

API Navegable
![API Navegable]()

Listado de productos
![Listado de productos]()

Panel de Administración
![Panel de Administración]()

Documentación Swagger
![Documentación Swagger]()

Documentación Redoc
![Documentación Redoc]()
