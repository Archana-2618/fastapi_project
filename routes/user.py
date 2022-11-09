from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import *

user = APIRouter()

@user.get("/")
async def read_data():
    return conn.execute(users.select()).fetchall()

@user.get("/id")
async def read_data(id:int):
    return conn.execute(users.select().where(users.c.id ==id)).fetchall()

@user.post("/")
async def write_data(user:User):
    conn.execute(users.insert().values(
        Address1=user.Address1,
        Address2=user.Address2,
        City=user.City,
        ZipCode=user.ZipCode,
    )).fetchall()

@user.put("/{id}")
async def update_data(id:int,user:User):
    conn.execute(users.update().values(
        Address1=user.Address1,
        Address2=user.Address2,
        City=user.City,
        ZipCode=user.ZipCode
    ).wehere(users.c.id==id))
    return conn.execute(users.select()).fetchall()

@user.delete("/")
async def delete_data():
    conn.execute(users.delete().where(users.c.id==id))
    return conn.execute(users.select()).fetchall()

