"""A simple Hello World FastAPI application"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello():
    """A simple Hello World GET request"""
    return {"message": "Hello, World!"}


@app.get("/api")
async def api():
    """A simple Hello World GET request"""
    return {"message": "Hello, /api!"}
