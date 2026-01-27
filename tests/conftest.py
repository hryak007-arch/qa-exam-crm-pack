import os
import tempfile
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Очікувана структура застосунку згідно звіту:
# app/main.py   -> app = FastAPI()
# app/db.py     -> get_db()
# app/models.py -> Base

from app.main import app
from app.db import get_db
from app.models import Base


@pytest.fixture(scope="session")
def db_engine():
    """Тимчасова SQLite БД на час тест-сесії."""
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    engine = create_engine(f"sqlite:///{path}", connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    yield engine
    engine.dispose()
    try:
        os.remove(path)
    except OSError:
        pass


@pytest.fixture()
def db_session(db_engine):
    """SQLAlchemy session для кожного тесту."""
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(db_session):
    """FastAPI TestClient з override залежності get_db()."""

    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
