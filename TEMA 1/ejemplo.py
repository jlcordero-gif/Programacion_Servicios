from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# --- 1. Entidad User  ---
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

app = FastAPI()

# --- 2. Base de Datos Simulada ---
# Los IDs se asignan aquí, por lo que no son opcionales en la lista
users_list: List[User] = [
    User(id=1, name="Paco", surname="Pérez", age=30),
    User(id=2, name="María", surname="Martínez", age=20),
    User(id=3, name="Lucía", surname="Rodríguez", age=40)
]

# --- 3. Funciones Auxiliares ---

def search_user(id: int) -> User:
    """Busca un usuario por id en la lista. Lanza 404 si no lo encuentra."""
    users = [u for u in users_list if u.id == id]
    
    if not users:
        raise HTTPException(status_code=404, detail="User not found")
        
    return users[0]

def next_id() -> int:
    """Calcula el id máximo actual y le suma 1."""
    if not users_list:
        return 1
    # Usamos lambda para obtener el id máximo correctamente
    return max(users_list, key=lambda u: u.id).id + 1


# --- 4. Endpoints (Rutas) ---

# GET para obtener la lista completa de usuarios
@app.get("/users", response_model=List[User])
def users():
    return users_list

# GET para obtener un usuario por ID
@app.get("/users/{id}", response_model=User)
def get_user(id: int): 
    return search_user(id)

# POST para añadir un nuevo usuario
# Usamos el modelo 'User' directamente como tipo de dato (sin UserInput)
@app.post("/users", status_code=201, response_model=User)
def add_user(user: User): # ¡Usamos User aquí!
    
    # Calculamos nuevo id y lo modificamos al usuario a añadir (user.id = next_id())
    user.id = next_id()
    
    users_list.append(user)

    # La respuesta de nuestro método es el propio usuario añadido (return user)
    return user

@app.put("/users/{id}", response_model=User)
def modify_user(id: int, user: User):
    
    # Buscamos el índice y el usuario guardado
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            # 1. user.id = id (Aseguramos que el ID del objeto sea el de la ruta)
            user.id = id
            
            # 2. users_list[index] = user (Reemplazamos el objeto en la lista)
            users_list[index] = user
            
            # 3. return user
            return user
            
    # Si el bucle termina sin encontrarlo, lanzamos 404
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{id}")
def delete_user(id: int):
    
    # Buscamos el usuario guardado para eliminarlo
    for saved_user in users_list:
        if saved_user.id == id:
            # users_list.remove(saved_user)
            users_list.remove(saved_user)
            
            # return {} (respuesta vacía para DELETE exitoso)
            return {} 

    # Si el bucle termina sin encontrarlo, lanzamos 404
    raise HTTPException(status_code=404, detail="User not found")
# --- Cómo Ejecutar ---
# Ejecuta con: uvicorn main:app --reload