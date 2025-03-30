from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, Componente
from models import ComponenteCreate, ComponenteOut

app = FastAPI()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/componentes/", response_model=ComponenteOut)
def crear_componente(componente: ComponenteCreate, db: Session = Depends(get_db)):
    db_componente = Componente(**componente.dict())
    db.add(db_componente)
    db.commit()
    db.refresh(db_componente)
    return db_componente

@app.get("/componentes/", response_model=list[ComponenteOut])
def obtener_componentes(db: Session = Depends(get_db)):
    return db.query(Componente).all()

@app.get("/componentes/{componente_id}", response_model=ComponenteOut)
def obtener_componente(componente_id: int, db: Session = Depends(get_db)):
    componente = db.query(Componente).filter(Componente.id == componente_id).first()
    if componente is None:
        raise HTTPException(status_code=404, detail="Componente no encontrado")
    return componente
