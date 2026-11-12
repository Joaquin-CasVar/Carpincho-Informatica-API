# API Carpincho Informática
Backend de una tienda de informática y hardware que permite carga, lectura, actualización y borrado de productos, ventas y usuarios. Otras funcionalidades incluyen un panel de administración, configuración de Docker y documentación estándar (OpenAPI Specification)

## Integrantes
- [Valentino Alcaraz](https://github.com/Alquita)
- [Joaquín Castellano](https://github.com/Joaquin-CasVar)
- [Esteban Ordoñez](https://github.com/estebanordonezz)

### Deploy en Render
La aplicación está desplegada a través de [Render](https://carpincho-informatica-api.onrender.com)

### Proyecto frontend que consume la API
[Repositorio](https://github.com/Joaquin-CasVar/Carpincho-Informatica-Next.js) - [Despliegue en Vercel](https://carpincho-informatica-next-js-lemon.vercel.app)

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

#### Tablero Kanban de organización del proyecto
[GitHub Projects](https://github.com/users/Joaquin-CasVar/projects/4/views/1)

---

## Diagrama de la Base de Datos
![Diagrama de la Base de Datos](https://i.imgur.com/F9nx59g.png)

---

## Proyecto funcionando
Ruta base
![Ruta base](https://i.imgur.com/9IjdDNN.png)

API Navegable
![API Navegable](https://i.imgur.com/WhLV3PT.png)

Listado de productos
![Listado de productos](https://i.imgur.com/HFRqVg3.png)

Panel de Administración
![Panel de Administración](https://i.imgur.com/RSabXwG.png)

Documentación Swagger
![Documentación Swagger](https://i.imgur.com/erwH8gX.png)

Documentación Redoc
![Documentación Redoc](https://i.imgur.com/Fof3i8e.png)
