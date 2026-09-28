from pydantic import BaseModel, ConfigDict, Field
#acá solo se coloca la emtrada de la API, no se colocan los outputs de la predicción

class CondicionesProceso(BaseModel):
    """Promedios horarios de los tres sensores de cada cámara."""

    model_config = ConfigDict(extra="forbid")

    T_camara_1: float = Field(ge=-200, le=800)
    T_camara_2: float = Field(ge=-1000, le=1400)
    T_camara_3: float = Field(ge=-800, le=2600)
    T_camara_4: float = Field(ge=-700, le=1300)
    T_camara_5: float = Field(ge=-200, le=1000)
    H_data: float = Field(ge=0, le=250)
    AH_data: float = Field(ge=0, le=20)
