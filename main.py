from contextlib import asynccontextmanager
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, Request, HTTPException


from esquemas import CondicionesProceso

#argar modelo, y @ le da un ciclo de vidaal proceso para descpmectar bundle al final
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.bundle = joblib.load(Path(__file__).with_name("modelo_calidad.joblib"))
    yield
    app.state.bundle = None

#Inicializamos API con metadatos y ciclo de vida
app = FastAPI(
    title="Predicción de calidad del proceso",
    description="Estima una medición de calidad a partir de condiciones horarias del proceso.",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/")
def estado(request: Request):
    return {"servicio": "Predicción de calidad", "modelo_cargado": request.app.state.bundle is not None}


@app.post("/predecir")
def predecir(datos: CondicionesProceso, request: Request):
    bundle = request.app.state.bundle
    entrada = pd.DataFrame([datos.model_dump()])[bundle["columnas"]]
    estimacion = float(bundle["modelo"].predict(entrada)[0])
    return {
        "calidad_estimada": round(estimacion, 3), 
        "unidad": "unidad original de quality (no especificada)"
        }
