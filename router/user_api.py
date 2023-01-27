from schemas import UserBase, UserDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db_session
from db import user


router = APIRouter(
  prefix='/user',
  tags=['user']
)

# Create user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db_session)):
    return user.create_user(db, request)

# Read users
@router.get('/', response_model=list[UserDisplay])
def get_users(db: Session = Depends(get_db_session)):
    return user.get_all_users(db)

@router.get('/{id}', response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db_session)):
    return user.get_user(db, id)


# Update user
@router.put('/{id}')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db_session)):
    return user.update_user(db, id, request)



# Delete user
@router.delete('/{id}')
def delete_user(id: int, db: Session = Depends(get_db_session)):
    return user.delete_user(db, id)
