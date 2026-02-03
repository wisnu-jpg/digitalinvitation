from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "Andi"},
        {"id": 2, "name": "Budi"}
    ]
@app.get("/users/{user}")
def get_user(user: str):
    return {"name": user}

# skema User
class User(BaseModel):
    name: str
    email: str

@app.post("/users")
def create_user(userdata: User):
    return userdata

#skema tugas
class products(BaseModel):
    id: int
    name: str
    price: str

@app.post("/products")
def create_product(productdata: products):
    return productdata