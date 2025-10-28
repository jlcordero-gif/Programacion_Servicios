from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional


#entidades 
class Persona(BaseModel):
    Id: int
    DNI: str
    Nombre: str
    ApellIdos: str
    Telefono: str
    Correo: str

class Movil(BaseModel):
    Id: int
    PrecioCoste: float
    PrecioVenta: float
    IdPersona: int 


class MovilInput(BaseModel):
    PrecioCoste: float
    PrecioVenta: float
    IdPersona: int

app = FastAPI()

#listas

personas_list: List[Persona] = [
    Persona(Id=1, DNI="12345678A", Nombre="Juan", ApellIdos="Pérez García", Telefono="600112233", Correo="juan.perez@example.com"),
    Persona(Id=2, DNI="87654321B", Nombre="María", ApellIdos="Gómez López", Telefono="611223344", Correo="maria.gomez@example.com"),
    Persona(Id=3, DNI="00000000Z", Nombre="Carlos", ApellIdos="Martínez", Telefono="633445566", Correo="carlos.m@example.com")
]

moviles_list: List[Movil] = [
    Movil(Id=101, PrecioCoste=150.00, PrecioVenta=250.00, IdPersona=1), # Móvil de Juan
    Movil(Id=102, PrecioCoste=300.00, PrecioVenta=450.00, IdPersona=1), # Otro de Juan
    Movil(Id=103, PrecioCoste=50.00, PrecioVenta=100.00, IdPersona=3)  # Móvil de Carlos
]

#funciones
def search_persona(Id: int) -> Persona:
    for p in personas_list:
        if p.Id == Id:
            return p
    raise HTTPException(status_code=404, detail="Persona not found")

def next_Id_persona() -> int:
    return max(personas_list, key=lambda p: p.Id).Id + 1 if personas_list else 1

def search_movil(Id: int) -> Movil:
    for m in moviles_list:
        if m.Id == Id:
            return m
    raise HTTPException(status_code=404, detail="Movil not found")

def next_Id_movil() -> int:
    return max(moviles_list, key=lambda m: m.Id).Id + 1 if moviles_list else 1

# endpoint general

@app.get("/")
def root():
    return {"mensaje": "Bienvenido a la API de Personas y Móviles"}

# endpoints personas

@app.get("/personas", response_model=List[Persona])
def personas():
    return personas_list

@app.get("/personas/{Id}", response_model=Persona)
def get_persona(Id: int): 
    return search_persona(Id)

@app.post("/personas", status_code=201, response_model=Persona)
def add_persona(persona: Persona): 
    persona.Id = next_Id_persona() 
    personas_list.append(persona)
    return persona

@app.put("/personas/{Id}", response_model=Persona)
def modify_persona(Id: int, persona: Persona):
    for index, saved_persona in enumerate(personas_list):
        if saved_persona.Id == Id:
            persona.Id = Id
            personas_list[index] = persona
            return persona
            
    raise HTTPException(status_code=404, detail="Persona not found")


@app.delete("/personas/{Id}")
def delete_persona(Id: int):
    
    for saved_persona in personas_list:
        if saved_persona.Id == Id:
            personas_list.remove(saved_persona)
            return {} 

    raise HTTPException(status_code=404, detail="Persona not found")

# endpoiints moviles

@app.get("/moviles", response_model=List[Movil])
def get_all_moviles():
    return moviles_list

@app.get("/moviles/{Id}", response_model=Movil)
def get_movil(Id: int):
    return search_movil(Id)

@app.post("/moviles", status_code=201, response_model=Movil)
def add_movil(movil_data: MovilInput):
    try:
        search_persona(movil_data.IdPersona)
    except HTTPException:
        raise HTTPException(status_code=400, detail=f"IdPersona {movil_data.IdPersona} does not exist.")
        
    new_id = next_Id_movil()
    
    new_movil = Movil(
        Id=new_id, 
        PrecioCoste=movil_data.PrecioCoste,
        PrecioVenta=movil_data.PrecioVenta,
        IdPersona=movil_data.IdPersona
    )
    
    moviles_list.append(new_movil)
    return new_movil

@app.put("/moviles/{Id}", response_model=Movil)
def modify_movil(Id: int, movil_data: MovilInput):
    try:
        search_persona(movil_data.IdPersona)
    except HTTPException:
        raise HTTPException(status_code=400, detail=f"IdPersona {movil_data.IdPersona} does not exist.")
        
    for index, saved_movil in enumerate(moviles_list):
        if saved_movil.Id == Id:
            movil_to_save = Movil(
                Id=Id,
                PrecioCoste=movil_data.PrecioCoste,
                PrecioVenta=movil_data.PrecioVenta,
                IdPersona=movil_data.IdPersona
            )
            moviles_list[index] = movil_to_save
            return movil_to_save
            
    raise HTTPException(status_code=404, detail="Movil not found")

@app.delete("/moviles/{Id}")
def delete_movil(Id: int):
    for saved_movil in moviles_list:
        if saved_movil.Id == Id:
            moviles_list.remove(saved_movil)
            return {} 

    raise HTTPException(status_code=404, detail="Movil not found")


#ejecutar
#fastapi dev main.py
