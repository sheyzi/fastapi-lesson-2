from typing import List, Optional
from unicodedata import category
from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    descriprion: Optional[str] = None
    price: float
    category_id: int

class ItemOut(ItemBase):
    id: int

    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    name: Optional[str] = None
    description: Optional[str] = None

class CategoryOut(CategoryBase):
    id: int

    class Config:
        orm_mode = True

class CategoryOutWithItems(CategoryBase):
    id: int
    items: List[ItemOut]

    class Config:
        orm_mode = True