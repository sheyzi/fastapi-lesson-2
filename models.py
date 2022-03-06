from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey

Base = declarative_base()


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(Text, nullable=True)

    items = relationship("Item", back_populates="category")

    def __repr__(self):
        return f"<Category name={self.name}>"


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("category_id"))

    category = relationship("Category", back_populates="items")

    def __repr__(self):
        return f"<Item name={self.name}>"
