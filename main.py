from fastapi import FastAPI
from router import blog_api
from router import user_api
from router import article_api
from db.database import engine
from db import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(user_api.router)
app.include_router(blog_api.router)
app.include_router(article_api.router)

@app.get('/hello')
def hello():
    return {'message': 'Hello world'}

models.Base.metadata.create_all(engine)

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