from fastapi import FastAPI
from router import blog_api

app = FastAPI()
app.include_router(blog_api.router)

@app.get('/hello')
def hello():
    return {'message': 'Hello world'}

