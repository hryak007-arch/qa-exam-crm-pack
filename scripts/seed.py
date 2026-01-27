"""Seed-скрипт (приклад/шаблон).
Потрібно адаптувати під ваші моделі/поля, якщо вони відрізняються.
"""

from app.db import SessionLocal
from app.models import Client, Order, StatusLog

def main():
    db = SessionLocal()
    try:
        c1 = Client(full_name="Клієнт Seed 1", phone="+380500000010", email="seed1@example.com", address="Суми")
        db.add(c1)
        db.commit()
        db.refresh(c1)

        o1 = Order(client_id=c1.id, device="iPhone 12", problem="Заміна акумулятора", price=1500, status="new")
        db.add(o1)
        db.commit()
        db.refresh(o1)

        log = StatusLog(order_id=o1.id, old_status="new", new_status="in_progress")
        db.add(log)
        db.commit()

        print("Seed data inserted OK")
    finally:
        db.close()

if __name__ == "__main__":
    main()
