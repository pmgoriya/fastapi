from fastapi import FastAPI, HTTPException, Query
from database.db import create_connection, create_tables
from schemas.schemas import UserCreate, FarmerCreate
import sqlite3


app = FastAPI()

@app.on_event("startup")
async def startup_event():
    conn = create_connection()
    create_tables(conn)

@app.get("/users/")
async def read_users(role: str = Query(..., description="User role")):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Insufficient permissions")
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return {"users": users}   

@app.post("/users/")
async def create_user(user: UserCreate):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (email, password, role) VALUES (?, ?, ?)", (user.email, user.password, user.role))
    conn.commit()
    return {"message": "User created successfully"}

@app.post("/farmers/")
async def create_farmer(farmer: FarmerCreate):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO farmers (Name, Annual_Income, Contact, land, gender) VALUES (?, ?, ?, ?, ?)",
                   (farmer.Name, farmer.Annual_Income, farmer.Contact, farmer.land, farmer.gender))
    conn.commit()
    return {"message": "Farmer created successfully"}

@app.get("/farmers/")
async def read_farmers(role: str = Query(..., description="User role")):
    if role != "operation":
        raise HTTPException(status_code=403, detail="Insufficient permissions")
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM farmers")
    farmers = cursor.fetchall()
    return {"farmers": farmers}


