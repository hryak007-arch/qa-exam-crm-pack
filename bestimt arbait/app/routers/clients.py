from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..db import get_db
from .. import schemas, crud

router = APIRouter(prefix="/clients", tags=["clients"])

@router.post("", response_model=schemas.ClientRead, status_code=status.HTTP_201_CREATED)
def create_client(payload: schemas.ClientCreate, db: Session = Depends(get_db)):
    return crud.create_client(db, payload)
