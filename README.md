# Proyecto final: predicción de calidad

El notebook une mediciones del proceso por minuto con mediciones horarias de `quality`, agrega tres sensores en cada una de cinco cámaras y calcula promedios por hora. La asociación con `quality` supone una hora de tránsito por la máquina; es una hipótesis del proyecto que requiere confirmación del origen de los datos.

## Datos y evaluación

Coloca `data_X.csv` y `data_Y.csv` junto al notebook y ejecútalo de inicio a fin. Usa siete entradas y una separación cronológica de 80 % para entrenamiento y 20 % para prueba. `sample_submission.csv` contiene predicciones de ejemplo y no se usa como verdad de referencia. El bundle `modelo_calidad.joblib` contiene modelo, columnas, rangos observados, métricas, fecha y versiones.

El contrato de la API espera **promedios horarios ya calculados**, no lecturas instantáneas de sensores. Los límites de Pydantic son controles amplios de integridad; el modelo no está validado para cualquier combinación de valores dentro de ellos. La salida conserva la escala original de `quality`, cuya unidad física no consta en los archivos.

## API y contenedor

```bash
docker build -t modelo-calidad .
docker run --rm -p 8000:8000 modelo-calidad
```

Abre `http://localhost:8000/docs`. Prueba `GET /` y `POST /predecir` con este caso válido:

```json
{"T_camara_1": 211, "T_camara_2": 350, "T_camara_3": 476, "T_camara_4": 350, "T_camara_5": 242, "H_data": 165, "AH_data": 9.2}
```

Para obtener 422, cambia `H_data` por `-1`. Guarda capturas del JSON enviado, código HTTP y respuesta en `capturas/`. El modelo no define límites de aceptación de producto y la predicción no constituye una decisión de liberación.
