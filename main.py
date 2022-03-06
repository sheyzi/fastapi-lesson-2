from fastapi import FastAPI, HTTPException, status, Depends
from typing import Optional, List
from pydantic import BaseModel

from sqlalchemy.orm import Session

from db import get_db
from models import Category
from schemas import CategoryCreate, CategoryOut, CategoryOutWithItems, CategoryUpdate

app = FastAPI()

@app.post("/category/create/", status_code=201, response_model=CategoryOut, tags=["Category"])
def create_category(body: CategoryCreate,db: Session = Depends(get_db)):
    category = Category(
        name=body.name,
        description=body.description
    )
    db.add(category)
    db.commit()
    db.refresh(category)
    return category
    
@app.get("/category/all/", response_model=List[CategoryOut], tags=["Category"])
def get_all_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).all()
    return categories



@app.get('/category/{id}/', response_model=CategoryOutWithItems, tags=["Category"])
def get_category_with_id(id: int, db: Session = Depends(get_db)):
    category = db.query(Category).get(id)
    if not category:
        raise HTTPException(404, f"Category with id {id} doesn't exist!")
    return category


@app.delete('/category/{id}/', tags=["Category"])
def delete_category(id: int, db: Session = Depends(get_db)):
    category = db.query(Category).get(id)
    if not category:
        raise HTTPException(404, f"Category with id {id} doesn't exist!")
    db.delete(category)
    db.commit()
    return {"msg": "Done!"}


@app.put('/category/{id}/', tags=["Category"])
def update_category(id: int, body: CategoryUpdate,db: Session = Depends(get_db)):
    body = body.dict()
    filtered_body = {}
    
    for key, value in body.items():
        if value:
            filtered_body[key] = value
    
    if not filtered_body:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Nothing to update!")
    
    category = db.query(Category).filter(Category.id == id)
    if not category:
        raise HTTPException(404, f"Category with id {id} doesn't exist!")

    category.update(filtered_body)
    db.commit()
    updated_category = db.query(Category).get(id)
    return updated_category
    
    
# /post/all/ - GET
# /post/{id}/ - GET
# /post/create/ - POST
# /post/{id}/ - DELETE
# /post/{id}/ - PUT

