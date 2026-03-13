from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

lista_inscritos = []


class Mensaje(BaseModel):
    nombre: str


@app.post("/inscripcion")
def realizar_inscripcion(mensaje: Mensaje):
    lista_inscritos.append(mensaje.nombre)
    return {"inscripcion": "Exitosa", "sr/sra": mensaje.nombre}


@app.get("/inscripciones")
def obtener_todas_las_inscripciones():
    return {"total_inscritos": len(lista_inscritos), "inscritos": lista_inscritos}
