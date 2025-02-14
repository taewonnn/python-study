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
# "Rick"
# ,
# "Morty"
# ]
@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]



fake_items_db = [{"item_name": "Baz"},{"item_name": "Baz"},{"item_name": "Baz"},{"item_name": "Baz"},{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"},{"item_name": "Baz"},{"item_name": "Baz"},{"item_name": "Baz"},{"item_name": "Baz"},{"item_name": "Baz"},{"item_name": "Baz"},{"item_name": "Baz"},{"item_name": "Baz"},{"item_name": "Baz"},{"item_name": "Baz"},{"item_name": "Baz"},{"item_name": "Baz"}]
@app.get('/items/')
async def read_item(skip: int = 0, limit: int =10):
    return fake_items_db[skip: skip + limit]