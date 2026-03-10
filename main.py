from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Mensaje(BaseModel):
    texto: str


@app.post("/eco")
def repetir_mensaje(mensaje: Mensaje):
    return {"estado": "Éxito", "mensaje_recibido": mensaje.texto}
