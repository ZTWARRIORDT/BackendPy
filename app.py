from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35), User(id=2, name="Moure", surname="Dev", url="https://mouredev.com", age=35), User(id=3, name="Brais", surname="Dahlberg", url="https://haakon.com", age=33)]

@app.get("/users")
async def users():
    return users_list

@app.get("/user/{id}")
async def user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}


@app.get("/userquery/")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}