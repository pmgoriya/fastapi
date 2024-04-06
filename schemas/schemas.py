from pydantic import BaseModel
from enum import Enum

class Role(str, Enum):
    admin = "admin"
    operation = "operation"
class Gender(str, Enum):
    male = "M"
    female = "F"

class UserCreate(BaseModel):
    email: str
    password: str
    role: Role

class FarmerCreate(BaseModel):
    Name: str
    Annual_Income: int
    Contact: int
    land: int
    gender: Gender





