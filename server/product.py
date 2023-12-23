from sqlalchemy.orm import DeclarativeBase

from sqlalchemy import Column, Integer, Text, String
from sqlalchemy.orm import Mapped


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String(255), nullable=False)
    description: Mapped[str] = Column(Text, nullable=False)
    price: Mapped[float] = Column(Integer, nullable=False)
    image_url: Mapped[str] = Column(String(255), nullable=False)
    stock: Mapped[int] = Column(Integer, nullable=False)
