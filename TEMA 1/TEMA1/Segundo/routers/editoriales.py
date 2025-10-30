from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional


router = APIRouter(tags= ["Editoriales"])


#entidades 
class Editorial(BaseModel):
    Id: int
    CIF: str
    RazonSocial: str
    Dirección: str
    Web: str
    Correo: str
    Teléfono: str

#listas

editoriales_list: List[Editorial] = [
    Editorial(
        Id=1, 
        CIF="B87654321", 
        RazonSocial="Ediciones Clásicas S.A.", 
        Dirección="Calle Falsa 123", 
        Web="www.clasicas.com", 
        Correo="info@clasicas.com", 
        Teléfono="910000000"
    ),
    Editorial(
        Id=2, 
        CIF="A12345678", 
        RazonSocial="Literatura Moderna SL", 
        Dirección="Avenida Principal 45", 
        Web="www.moderna.es", 
        Correo="contacto@moderna.es", 
        Teléfono="931111111"
    )
    ]

#funciones
def search_editorial(Id: int) -> Editorial:
    for e in editoriales_list:
        if e.Id == Id:
            return e
    raise HTTPException(status_code=404, detail="Editorial not found")

def next_Id_editorial() -> int:
    return max(editoriales_list, key=lambda p: p.Id).Id + 1 if editoriales_list else 1


# endpoints eeditoriales

@router.get("/editoriales", response_model=List[Editorial])
def editorials():
    return editoriales_list

@router.get("/editorials/{Id}", response_model= Editorial)
def get_editorial(Id: int): 
    return search_editorial(Id)

@router.post("/editorials", status_code=201, response_model= Editorial)
def add_editorial(editorial: Editorial): 
    editorial.Id = next_Id_editorial() 
    editoriales_list.append(Editorial)
    return editorial

@router.put("/editorials/{Id}", response_model=Editorial)
def modify_editorial(Id: int, editorial: Editorial):
    for index, saved_editorial in enumerate(editoriales_list):
        if saved_editorial.Id == Id:
            editorial.Id = Id
            editoriales_list[index] = editorial
            return editorial
            
    raise HTTPException(status_code=404, detail="Editorial not found")


@router.delete("/editorials/{Id}")
def delete_editorial(Id: int):
    
    for saved_editorial in editoriales_list:
        if saved_editorial.Id == Id:
            editoriales_list.remove(saved_editorial)
            return {} 

    raise HTTPException(status_code=404, detail="Editorial not found")