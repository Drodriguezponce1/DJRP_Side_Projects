from fastapi import FastAPI
import db
from fastapi import HTTPException

app = FastAPI() 

conn = db.connect()
cursor = conn.cursor()

@app.on_event("startup")
async def initialize():
    db.initialize_db()


@app.get("/all/")
async def read_all_tables():
    x = db.show_tables()
    return {"Tables" : x} 

@app.get("/all_users/")
async def read_all_users():
    x = db.show_users()
    return {"All Users" : x} 


@app.post("/add/")
async def add_user(fname:str, lname:str):
    uId = db.add_person(fname, lname)

    if uId:
        return {"User Id": uId, "First Name": fname, "Last Name": lname}
    else:
        raise HTTPException(status_code=400, detail="User not created")

'''
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/test/{x}&{y}")
def sum(x:int,y:int,z:int = 0):
    return x + y + z'''