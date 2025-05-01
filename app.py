from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")  # Scenario 1
async def hello():
    return "hello"

@app.get("/hello/{name}")  #Scenario 2
async def hello_name(name):
    return f"Welcome to the Fast API journey {name}"

#Scenario 3
food_items = {  #food_items dictionary
    'srilankan': [ "Kottu", "Rice"],
    'indian': [ "Dosa", "Poori" ],
    'american': [ "Burger", "Pie"]
}

@app.get("/get_items/{cuisine}")
async def get_item(cuisine):
    # return food_items.get(cuisine)
    return f"{cuisine} cuisine has {food_items.get(cuisine)}"
