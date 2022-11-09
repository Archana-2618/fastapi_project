from sqlalchemy import *
from config.db import meta

users=Table(
    'users', meta,
    Column('id',Integer,primary_key=True),
    Column('Address1',String(255)),
    Column('Address2',String(255)),
    Column('City',String(255)),
    Column('ZipCode',String(255)),

)
