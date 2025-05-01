from fastapi import FastAPI
from enum import Enum

app = FastAPI()

## in built data validation feature used

#Scenario 4
class AvailableCuisines(str, Enum):
    srilankan = "srilankan"
    indian = "indian"
    american = "american"
    
food_items = {  #food_items dictionary
    'srilankan': [ "Kottu", "Rice"],
    'indian': [ "Dosa", "Poori" ],
    'american': [ "Burger", "Pie"]
}

@app.get("/get_items/{cuisine}")
async def get_item(cuisine: AvailableCuisines):
    return f"{cuisine} cuisine has {food_items.get(cuisine)}"


#Scenario 5
coupon_code = {
    1 : '15%',
    2 : '25%',
    3 : '60%'
}

@app.get("/get_coupon/{code}")
async def get_code(code: int):
    return { 'Discount percentage is ': coupon_code.get(code) }