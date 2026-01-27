from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..db import get_db
from .. import schemas, crud

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("", response_model=schemas.OrderRead, status_code=status.HTTP_201_CREATED)
def create_order(payload: schemas.OrderCreate, db: Session = Depends(get_db)):
    try:
        order = crud.create_order(db, payload)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return order

@router.get("", response_model=list[schemas.OrderRead])
def list_orders(status: str | None = None, db: Session = Depends(get_db)):
    return crud.list_orders(db, status=status)

@router.get("/{order_id}", response_model=schemas.OrderRead)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = crud.get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/{order_id}/status", response_model=schemas.OrderRead)
def change_status(order_id: int, body: dict, db: Session = Depends(get_db)):
    new_status = body.get("new_status")
    if not new_status:
        raise HTTPException(status_code=400, detail="new_status is required")
    try:
        order = crud.change_order_status(db, order_id, new_status)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
