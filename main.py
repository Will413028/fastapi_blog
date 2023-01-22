from fastapi import FastAPI, status, Response
from typing import Optional
from enum import Enum

class BlogType(str, Enum):
    short= 'short'
    story= 'story'
    howto= 'howto'

app = FastAPI()


@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'Blog type id {type}'}


def hello():
    return {'message': 'Hello world'}


@app.get('/hello')
def hello():
    return {'message': 'Hello world'}


@app.get('/blog/all', tags=['blog'], summary="Retrieve all blogs", description="This api call simuates fetching all blogs")
def get_all_blog(page = 1, page_size: Optional[int] = None):
    return {'message': f'All {page_size} blogs on page {page}'}


@app.get('/blog/{id}/comments/{comment_id}', tags=['comments'])
def get_comment(id:int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulates retrieving a comment of a blog

    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **vaild** optional query parameter
    - **username** optional query parameter

    """
    return {'message': f'blog_id {id},  comment_id {comment_id}, valid {valid}, username {username}   '}


@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def get_blog(id:int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': f'Blog {id} not found'}
    else :
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id {id}'}


