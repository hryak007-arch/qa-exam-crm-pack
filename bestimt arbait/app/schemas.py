from datetime import datetime
from typing import Optional, List, Dict
from pydantic import BaseModel, Field

# --- Clients ---
class ClientCreate(BaseModel):
    full_name: str = Field(min_length=1)
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None

class ClientRead(ClientCreate):
    id: int
    class Config:
        from_attributes = True

# --- Status log ---
class StatusLogRead(BaseModel):
    id: int
    old_status: Optional[str] = None
    new_status: str
    changed_at: datetime

    class Config:
        from_attributes = True

# --- Orders ---
class OrderCreate(BaseModel):
    client_id: int
    device: str = Field(min_length=1)
    problem: Optional[str] = None
    price: Optional[float] = None

class OrderRead(BaseModel):
    id: int
    client_id: int
    device: str
    problem: Optional[str] = None
    price: Optional[float] = None
    status: str
    created_at: datetime
    status_log: List[StatusLogRead] = []

    class Config:
        from_attributes = True

# --- Reports ---
class ReportPeriod(BaseModel):
    date_from: str
    date_to: str
    total_orders: int
    total_revenue: float
    by_status: Dict[str, int]
