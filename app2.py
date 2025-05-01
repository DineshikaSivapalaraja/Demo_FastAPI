from fastapi import FastAPI

app = FastAPI()

#Scenario 6 --> Create basic FastAPI app with RESTful API endpoints
fruit_items = ["apple", "orange", "pine apple"]

@app.get('/fruit')
async def get_fruit_list():
    return fruit_items

@app.post('/add_fruit/{fruit}')
async def post_fruit(fruit: str):
    if fruit not in fruit_items:
        # fruit_items.append("mango")
        fruit_items.append(fruit)
        return fruit_items
    else:
        return f"{fruit} already in the fruit list"

@app.delete('/delete_fruit/{fruit}')
async def remove_fruit(fruit: str):
    if fruit in fruit_items:
        fruit_items.remove(fruit)
        return fruit_items
    else:
        return f"{fruit} is not available in the list"

@app.put('/update_fruits/{fruit}')
async def update_fruit(fruit: str):
    if fruit in fruit_items:
        index = fruit_items.index(fruit)
        fruit_items[index]  = "mango"
        #fruit = "mango"
        return fruit_items
    else:
        return "The fruit is not available"


