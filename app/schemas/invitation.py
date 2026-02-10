from pydantic import BaseModel, Field
class invitation(BaseModel):
    title: str = Field(..., max_length=15)
    event_date: str
    location: str
    is_public: bool = True

# skema User
class User(BaseModel):
    name: str
    email: str
