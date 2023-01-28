from typing import List
from schemas import ArticleBase, ArticleDisplay, UserBase
from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from db.database import get_db_session
from db import article

router = APIRouter(
  prefix='/article',
  tags=['article']
)

# Create article
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db_session)):
  return article.create_article(db, request)

# Get specific article
@router.get('/{id}') #, response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db_session)):
  return {
    'data': article.get_article(db, id)
  }


products = ['watch', 'camera', 'video']
@router.post('/new')
def create_test(name: str = Form(...)):
  products.append(name)
  return products