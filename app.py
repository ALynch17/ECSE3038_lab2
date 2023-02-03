from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins=[
    "https://ecse-week3-demo.netlify.app"
]

fake_database=[]



@app.get("/todos")
async def get_all_todos():
    return fake_database
"""
@app.post("/todos")
async def create_todo(request: Request):
    todo = await request.json()
    fake_database.append(todo)
    return todo
"""
