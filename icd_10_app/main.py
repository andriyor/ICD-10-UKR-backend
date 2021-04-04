from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/codes/", response_model=List[schemas.Item])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), parent: Optional[int] = None, search: Optional[str] = None):
    users = crud.get_codes(db, skip=skip, limit=limit, parent=parent, search=search)
    return users


@app.get("/codes/{code_id}", response_model=schemas.Item)
def read_user(code_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_code(db, code_id=code_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
