# FastAPI entrypoint
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'GenAI DevOps Assistant Running'}
