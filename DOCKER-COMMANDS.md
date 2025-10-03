# ⚡ Comandos Docker - Referencia Rápida

## 🚀 Comandos Básicos

### Iniciar proyecto
```powershell
docker-compose up -d                    # Iniciar servicios en background
docker-compose up                       # Iniciar con logs en consola
docker-compose up jupyter               # Iniciar solo Jupyter
docker-compose up streamlit             # Iniciar solo Streamlit
```

### Detener proyecto
```powershell
docker-compose stop                     # Detener servicios
docker-compose down                     # Detener y eliminar contenedores
docker-compose down -v                  # + Eliminar volúmenes
```

### Ver estado
```powershell
docker-compose ps                       # Ver servicios activos
docker ps                               # Ver todos los contenedores
docker ps -a                            # Ver todos (incluidos detenidos)
```

## 📋 Logs y Monitoreo

```powershell
docker-compose logs                     # Ver logs de todos los servicios
docker-compose logs -f                  # Ver logs en tiempo real
docker-compose logs -f jupyter          # Logs de Jupyter en tiempo real
docker-compose logs --tail=100 jupyter  # Últimas 100 líneas
docker stats                            # Ver uso de recursos
```

## 🔧 Construcción

```powershell
docker-compose build                    # Construir imágenes
docker-compose build --no-cache         # Construir sin cache
docker-compose build jupyter            # Construir solo Jupyter
docker-compose up -d --build            # Construir e iniciar
```

## 💻 Ejecutar Comandos

### Acceder a shell del contenedor
```powershell
docker-compose exec jupyter bash        # Acceder a terminal Jupyter
docker-compose exec streamlit bash      # Acceder a terminal Streamlit
docker-compose exec python-scripts bash # Acceder a terminal Scripts
```

### Ejecutar comandos Python
```powershell
# Ejecutar script Python
docker-compose exec jupyter python src/data_loader.py

# Python interactivo
docker-compose exec jupyter python

# Ejecutar con IPython
docker-compose exec jupyter ipython

# Ejecutar notebook desde terminal
docker-compose exec jupyter jupyter nbconvert --execute notebooks/01_EDA.ipynb
```

### Instalar paquetes
```powershell
# Instalar paquete temporal
docker-compose exec jupyter pip install pandas-profiling

# Listar paquetes instalados
docker-compose exec jupyter pip list

# Ver versión de paquete
docker-compose exec jupyter pip show pandas
```

## 📊 Gestión de Datos

### Copiar archivos
```powershell
# De PC a contenedor
docker cp archivo.csv sales-prediction-jupyter:/app/data/raw/

# De contenedor a PC
docker cp sales-prediction-jupyter:/app/data/processed/output.csv ./

# Ver archivos en contenedor
docker-compose exec jupyter ls -la /app/data/raw/
```

### Limpiar espacio
```powershell
# Limpiar contenedores detenidos
docker container prune

# Limpiar imágenes sin usar
docker image prune

# Limpiar todo lo no usado
docker system prune

# Limpiar TODO (cuidado!)
docker system prune -a --volumes
```

## 🔄 Reinicio y Actualización

```powershell
# Reiniciar servicios
docker-compose restart
docker-compose restart jupyter          # Reiniciar solo Jupyter

# Actualizar servicio
docker-compose up -d --build jupyter

# Recrear contenedor
docker-compose up -d --force-recreate jupyter
```

## 🔍 Inspección y Debug

### Inspeccionar contenedor
```powershell
docker inspect sales-prediction-jupyter
docker-compose exec jupyter env         # Ver variables de entorno
docker-compose exec jupyter pwd         # Ver directorio actual
docker-compose exec jupyter df -h       # Ver espacio en disco
```

### Verificar red
```powershell
docker network ls                       # Listar redes
docker network inspect sales-prediction-ml_sales-network
```

### Ver puertos
```powershell
docker-compose port jupyter 8888        # Ver puerto mapeado
docker port sales-prediction-jupyter    # Ver todos los puertos
```

## 📦 Imágenes

```powershell
# Listar imágenes
docker images

# Listar imágenes del proyecto
docker images | findstr sales-prediction

# Eliminar imagen
docker rmi sales-prediction-ml-jupyter

# Eliminar todas las imágenes del proyecto
docker images | findstr sales-prediction | ForEach-Object { docker rmi $_.Split()[2] }
```

## 🎯 Workflows Específicos

### Agregar nueva dependencia
```powershell
# 1. Editar requirements.txt
code requirements.txt

# 2. Reconstruir imagen
docker-compose build --no-cache

# 3. Reiniciar servicios
docker-compose up -d
```

### Ejecutar notebook completo
```powershell
docker-compose exec jupyter jupyter nbconvert \
    --to notebook \
    --execute \
    --inplace \
    notebooks/01_EDA.ipynb
```

### Backup de datos
```powershell
# Crear backup
docker run --rm -v ${PWD}/data:/backup alpine tar czf /backup/backup.tar.gz /backup

# Restaurar backup
docker run --rm -v ${PWD}/data:/backup alpine tar xzf /backup/backup.tar.gz
```

### Ejecutar script Python con argumentos
```powershell
docker-compose exec jupyter python src/models.py --train --epochs 100
```

## 🚨 Troubleshooting

### Puerto en uso
```powershell
# Windows - Ver qué usa el puerto
netstat -ano | findstr :8888

# Matar proceso
taskkill /PID <PID> /F
```

### Contenedor no inicia
```powershell
# Ver logs detallados
docker-compose logs jupyter

# Verificar docker-compose.yml
docker-compose config

# Verificar Dockerfile
docker-compose build --progress=plain
```

### Errores de permisos
```powershell
# Ejecutar como root
docker-compose exec -u root jupyter bash

# Cambiar permisos
docker-compose exec -u root jupyter chmod -R 777 /app/data
```

### Limpiar y empezar de nuevo
```powershell
# ADVERTENCIA: Esto elimina todo
docker-compose down -v
docker system prune -a
docker-compose build --no-cache
docker-compose up -d
```

## 💡 Tips Útiles

### Alias útiles (agregar a perfil PowerShell)
```powershell
# Ver/editar perfil
notepad $PROFILE

# Agregar estos alias:
function dc { docker-compose $args }
function dcup { docker-compose up -d }
function dcdown { docker-compose down }
function dclogs { docker-compose logs -f $args }
function dcexec { docker-compose exec $args }
```

### Variables de entorno temporales
```powershell
docker-compose exec -e MY_VAR=value jupyter python script.py
```

### Ver cambios en contenedor
```powershell
docker diff sales-prediction-jupyter
```

## 🎓 Comandos Avanzados

### Multi-stage builds
```powershell
# Construir stage específico
docker build --target production -t my-image .
```

### Healthcheck manual
```powershell
docker-compose exec jupyter wget --spider http://localhost:8888
```

### Export/Import contenedor
```powershell
# Exportar
docker export sales-prediction-jupyter > container.tar

# Importar
docker import container.tar new-image:tag
```

---

## 📚 Referencias

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose CLI](https://docs.docker.com/compose/reference/)
- Guía completa: [DOCKER.md](DOCKER.md)
- Inicio rápido: [QUICKSTART.md](QUICKSTART.md)

---

💡 **Tip**: Guarda este archivo como referencia o imprímelo!
