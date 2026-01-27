from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False, index=True)
    phone = Column(String, nullable=True, index=True)
    email = Column(String, nullable=True, index=True)
    address = Column(String, nullable=True)

    orders = relationship("Order", back_populates="client", cascade="all, delete-orphan")

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False, index=True)

    device = Column(String, nullable=False)
    problem = Column(String, nullable=True)
    price = Column(Float, nullable=True)

    status = Column(String, nullable=False, index=True, default="new")
    created_at = Column(DateTime, default=datetime.utcnow)

    client = relationship("Client", back_populates="orders")
    status_log = relationship("StatusLog", back_populates="order", cascade="all, delete-orphan")

class StatusLog(Base):
    __tablename__ = "status_log"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False, index=True)

    old_status = Column(String, nullable=True)
    new_status = Column(String, nullable=False)

    changed_at = Column(DateTime, default=datetime.utcnow)

    order = relationship("Order", back_populates="status_log")
