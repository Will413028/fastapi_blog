from typing import List
from schemas import ArticleBase, ArticleDisplay, UserBase
from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from db.database import get_db_session
from db import article
from auth.oauth2 import oauth2_schema, get_current_user

router = APIRouter(
  prefix='/article',
  tags=['article']
)

# Create article
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db_session), current_user: UserBase = Depends(get_current_user)):
  return article.create_article(db, request)

# Get specific article
@router.get('/{id}')
def get_article(id: int, db: Session = Depends(get_db_session), current_user: UserBase = Depends(get_current_user)):
  return {
    'data': article.get_article(db, id),
    'current_user': current_user
  }


products = ['watch', 'camera', 'video']
@router.post('/new')
def create_test(name: str = Form(...)):
  products.append(name)
  return products