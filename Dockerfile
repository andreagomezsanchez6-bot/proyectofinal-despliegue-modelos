
#Construir la imagen del servidor FastAPI
FROM python:3.12-slim

WORKDIR /app
ENV PYTHODONTWRITEBYTECODE=1
    PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["sh", "-c", "--host", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]
