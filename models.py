from pydantic import BaseModel

# Modelo para crear un nuevo componente
class ComponenteCreate(BaseModel):
    nombre: str
    tipo: str
    descripcion: str

# Modelo para la respuesta del componente
class ComponenteOut(BaseModel):
    id: int
    nombre: str
    tipo: str
    descripcion: str

    class Config:
        orm_mode = True
