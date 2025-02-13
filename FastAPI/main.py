from fastapi import FastAPI

app = FastAPI()

# http://127.0.0.1:8000/

# {
# "message": "Hello World"
# }

@app.get("/")
async def root():
    return {"message": "Hello World"}
  
  
# http://127.0.0.1:8000/items/poo
# {
# "items_id": "poo"
# }
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"items_id": item_id}
  
  
  

# http://127.0.0.1:8000/users
# [
# "Rick",
# "Morty"
# ]
@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]
