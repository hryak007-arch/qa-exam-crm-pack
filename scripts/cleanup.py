"""Cleanup-скрипт (приклад/шаблон).
Видаляє тестові записи, створені seed.py.
"""

from app.db import SessionLocal
from app.models import Client, Order, StatusLog

def main():
    db = SessionLocal()
    try:
        # дуже спрощено: видаляємо все з таблиць (для тестового середовища)
        db.query(StatusLog).delete()
        db.query(Order).delete()
        db.query(Client).delete()
        db.commit()
        print("Cleanup OK")
    finally:
        db.close()

if __name__ == "__main__":
    main()
