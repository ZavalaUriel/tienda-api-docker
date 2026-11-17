# Imagen base oficial de Python, version ligera
FROM python:3.12-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Primero solo las dependencias, para aprovechar la cache de capas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Despues el codigo de la API
COPY app/ ./app/

# Usuario sin privilegios para ejecutar la API
RUN useradd --create-home appuser
USER appuser

# Puerto en el que escucha la API dentro del contenedor
EXPOSE 8000

# Docker revisa cada 30 s que la API responda
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/salud')"

# Comando que se ejecuta al iniciar el contenedor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
