from pydantic import BaseModel

class User(BaseModel):
    Address1:str
    Address2:str
    City:str
    ZipCode:int