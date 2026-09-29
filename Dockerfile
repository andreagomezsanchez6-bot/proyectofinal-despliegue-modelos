
#Construir la imagen del servidor FastAPI
FROM python:3.12-slim
WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1


RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

#Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

#correr despliegue
CMD ["sh", "-c", "--host", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]
