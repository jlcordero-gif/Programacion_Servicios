from fastapi import FastAPI
from routers import ejemplo, Persona
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(ejemplo.router)
app.include_router(Persona.router)

app.mount("/static", StaticFiles(directory="static"), name= "static")

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a la API de Personas , Móviles y Usuarios"}
