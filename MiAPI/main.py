from fastapi import FastAPI, HTTPException
import json

app = FastAPI(title="API de Personas", version="1.0")

# Cargar datos
with open("personas.json", "r", encoding="utf-8") as f:
    personas = json.load(f)

# --- ENDPOINTS GET ---

@app.get("/")
def root():
    return {"mensaje": "Bienvenido a la API de Personas"}

@app.get("/personas")
def get_personas():
    return personas

@app.get("/personas/{id}")
def get_persona_por_id(id: int):
    for p in personas:
        if p["id"] == id:
            return p
    raise HTTPException(status_code=404, detail="Persona no encontrada")

@app.get("/personas/dni/{dni}")
def get_persona_por_dni(dni: str):
    for p in personas:
        if p["dni"] == dni:
            return p
    raise HTTPException(status_code=404, detail="Persona no encontrada")
