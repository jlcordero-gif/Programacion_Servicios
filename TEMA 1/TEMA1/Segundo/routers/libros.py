from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter(tags=["Libros"])

#ENTIDAD 

class Libro(BaseModel):
    Id: int
    Precio: str
    ISBN: str
    Título: str
    NumPaginas: str
    Temática: str
    IdEditorial: str

#LISTA (base de datos simulada)

libros_list: List[Libro] = [
    Libro(
        Id=1,
        Precio="19.99",
        ISBN="978-84-376-0494-7",
        Título="Cien años de soledad",
        NumPaginas="471",
        Temática="Realismo mágico",
        IdEditorial="1"
    ),
    Libro(
        Id=2,
        Precio="14.50",
        ISBN="978-84-670-5510-4",
        Título="Don Quijote de la Mancha",
        NumPaginas="863",
        Temática="Novela clásica",
        IdEditorial="2"
    )
]

#FUNCIONES AUXILIARES

def search_libro(Id: int) -> Libro:
    for libro in libros_list:
        if libro.Id == Id:
            return libro
    raise HTTPException(status_code=404, detail="Libro no encontrado")

def next_Id_libro() -> int:
    return max(libros_list, key=lambda p: p.Id).Id + 1 if libros_list else 1

#ENDPOINTS

@router.get("/libros", response_model=List[Libro])
def get_libros():
    """Obtener todos los libros"""
    return libros_list

@router.get("/libros/{Id}", response_model=Libro)
def get_libro(Id: int):
    """Obtener un libro por su Id"""
    return search_libro(Id)

@router.post("/libros", status_code=201, response_model=Libro)
def add_libro(libro: Libro):
    """Agregar un nuevo libro"""
    libro.Id = next_Id_libro()
    libros_list.append(libro)
    return libro

@router.put("/libros/{Id}", response_model=Libro)
def modify_libro(Id: int, libro: Libro):
    """Modificar un libro existente"""
    for index, saved_libro in enumerate(libros_list):
        if saved_libro.Id == Id:
            libro.Id = Id
            libros_list[index] = libro
            return libro
    raise HTTPException(status_code=404, detail="Libro no encontrado")

@router.delete("/libros/{Id}")
def delete_libro(Id: int):
    """Eliminar un libro"""
    for saved_libro in libros_list:
        if saved_libro.Id == Id:
            libros_list.remove(saved_libro)
            return {}
    raise HTTPException(status_code=404, detail="Libro no encontrado")