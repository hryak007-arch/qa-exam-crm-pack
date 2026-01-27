from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db import get_db
from .. import crud, schemas

router = APIRouter(prefix="/reports", tags=["reports"])

@router.get("/period", response_model=schemas.ReportPeriod)
def report_period(date_from: str, date_to: str, db: Session = Depends(get_db)):
    try:
        df = datetime.fromisoformat(date_from)
        dt = datetime.fromisoformat(date_to)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format, expected YYYY-MM-DD")

    total_orders, total_revenue, by_status = crud.report_period(db, df, dt)
    return schemas.ReportPeriod(
        date_from=date_from,
        date_to=date_to,
        total_orders=total_orders,
        total_revenue=total_revenue,
        by_status=by_status,
    )
