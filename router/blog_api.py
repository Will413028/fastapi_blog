from fastapi import APIRouter, status, Response, Query
from typing import Optional
from enum import Enum
from pydantic import BaseModel


class BlogType(str, Enum):
    short= 'short'
    story= 'story'
    howto= 'howto'


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]

router = APIRouter(
    prefix='/blog', 
    tags=['blog']
)


@router.get('/all',
    summary="Retrieve all blogs",
    description="This api call simuates fetching all blogs",
    response_description="The list of available blogs"
    )
def get_all_blog(page = 1, page_size: Optional[int] = None):
    return {'message': f'All {page_size} blogs on page {page}'}


@router.get('/{id}/comments/{comment_id}', tags=['comments'])
def get_comment(id:int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulates retrieving a comment of a blog

    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **vaild** optional query parameter
    - **username** optional query parameter

    """
    return {'message': f'blog_id {id},  comment_id {comment_id}, valid {valid}, username {username}   '}


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id:int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': f'Blog {id} not found'}
    else :
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id {id}'}

@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'Blog type id {type}'}


@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1 ):
    blog.title
    return {
        'id': id,
        'data': blog,
        'version': version
        }

@router.post('/new/{id}/comment')
def create_blog(blog: BlogModel, id: int, 
    comment_id: int = Query(None,
    title='id of the comment',
    description='description of the comment',
    deprecated=True
    ) 
    ):
    blog.title
    return {
        'id': id,
        'data': blog,
        'comment_id': comment_id
        }