from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime

from . import models, schemas

ALLOWED_STATUSES = {"new", "in_progress", "done", "cancelled"}

# --- Clients ---
def create_client(db: Session, payload: schemas.ClientCreate) -> models.Client:
    client = models.Client(**payload.dict())
    db.add(client)
    db.commit()
    db.refresh(client)
    return client

# --- Orders ---
def create_order(db: Session, payload: schemas.OrderCreate) -> models.Order:
    # Ensure client exists
    client = db.query(models.Client).filter(models.Client.id == payload.client_id).first()
    if not client:
        raise ValueError("Client not found")

    order = models.Order(**payload.dict(), status="new")
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def list_orders(db: Session, status: str | None = None):
    q = db.query(models.Order)
    if status:
        q = q.filter(models.Order.status == status)
    return q.order_by(models.Order.id.asc()).all()

def get_order(db: Session, order_id: int) -> models.Order | None:
    return db.query(models.Order).filter(models.Order.id == order_id).first()

def change_order_status(db: Session, order_id: int, new_status: str) -> models.Order | None:
    if new_status not in ALLOWED_STATUSES:
        raise ValueError("Invalid status")

    order = get_order(db, order_id)
    if not order:
        return None

    old = order.status
    order.status = new_status
    db.add(models.StatusLog(order_id=order.id, old_status=old, new_status=new_status))
    db.commit()
    db.refresh(order)
    return order

# --- Reports ---
def report_period(db: Session, date_from: datetime, date_to: datetime):
    # Orders created_at in [date_from, date_to]
    q = db.query(models.Order).filter(models.Order.created_at >= date_from, models.Order.created_at <= date_to)

    total_orders = q.count()
    total_revenue = q.with_entities(func.coalesce(func.sum(models.Order.price), 0.0)).scalar() or 0.0

    # by status
    rows = q.with_entities(models.Order.status, func.count(models.Order.id)).group_by(models.Order.status).all()
    by_status = {status: count for status, count in rows}

    return total_orders, float(total_revenue), by_status
