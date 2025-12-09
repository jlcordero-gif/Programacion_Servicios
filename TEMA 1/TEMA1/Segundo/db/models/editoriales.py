
from typing import Optional
from pydantic import BaseModel

# Entidad user
class Editoriales(BaseModel):
    id: Optional[str] = None
    CIF: str
    RazonSocial: str
    Dirección: str
    Web: str
    Correo: str
    Teléfono: str

