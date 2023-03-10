from fastapi import FastAPI, Request
from router import blog_api, user_api, article_api, file_api
from auth import authentication
from db.database import engine
from db import models
from fastapi.middleware.cors import CORSMiddleware
import time

app = FastAPI()
app.include_router(authentication.router)
app.include_router(user_api.router)
app.include_router(blog_api.router)
app.include_router(article_api.router)
app.include_router(file_api.router)

@app.get('/hello')
def hello():
    return {'message': 'Hello world'}

models.Base.metadata.create_all(engine)

@app.middleware("http")
async def add_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    response.headers['duration'] = str(duration)
    return response 


origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)