from fastapi import FastAPI
from routers import editoriales, libros
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(editoriales.router)
app.include_router(libros.router)

app.mount("/static", StaticFiles(directory="static"), name= "static")

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a la API de Editoriales y Libros"}
