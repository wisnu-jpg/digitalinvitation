from fastapi import FastAPI
from app.schemas.invitation import User, invitation

app = FastAPI()

# path patameter dan perhitungan sederhana
# http://127.0.0.1:8000/invitation/vip-001 reg-002
# array [] = [1,2,3,4]

def kategoriTamu(slug: str):
    pecah=slug.split("-")
    kategori=pecah[0]
    if kategori == "vip":
        return {
            "code-tamu": pecah[1],
            "kategori": "Vip"
        }
    elif kategori == "reg":
        return {
            "code-tamu": pecah[1],
            "kategori": "tamu"
        }
    else:
        return {
            "code-tamu": pecah[1],
            "kategori": "Tamu"}
@app.get("/invitation/{slug}")
def get_invitation(slug: str):
    return kategoriTamu(slug)
@app.get("/invitation/")
def list_invitation(limit: int = 10, published: bool = True):
    return {
        "limit": limit,
        "published": published
    }

#response model
@app.post("/invitation/")
def create_invitation(response_model:invitation):
    return {
        "title": response_model.title,
        "event_date": response_model.event_date,
        "location": response_model.location,
        "is_public": response_model.is_public
    }
@app.get("/")
async def root():
    return {"message": "Hello FUCK"}

@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "Andi"},
        {"id": 2, "name": "Budi"}
    ]
@app.get("/users/{user}")
def get_user(user: str):
    return {"name": user}


@app.post("/users")
def create_user(userdata: User):
    return userdata

#skema tugas
