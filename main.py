from fastapi import FastAPI

app = FastAPI()
products_list = []
buyers_list = []
purchased = {}


@app.get("/")
async def showMessage():
    return {"response": "this is the root. Nothing else"}


@app.get("/products")
async def getProducts():
    return products_list


@app.get("/buyers")
async def getBuyers():
    return buyers_list


@app.post("/buyers")
async def addBuyer(name: str):
    if isinstance(name, str) == True:
        if (name in buyers_list):
            return {"result:": "Duplicate entry"}
        else:
            buyers_list.append(name)
            return {"result:": "OK"}
    else:
        return {"result:": "error. Value must be string."}


@app.post("/products")
async def addProduct(name: str):
    if isinstance(name, str) == True:
        if (name in products_list):
            return {"result:": "Duplicate entry"}
        else:

            products_list.append(name)
            return {"result:": "OK"}
    else:
        return {"result:": "error. Value must be string."}


@app.post("/buyers/{buyer}")
async def buyProduct(buyer: str, prod_name: str):
    if buyer in buyers_list:
        if prod_name in products_list:
            if buyer in purchased:
                purchased[buyer] += 1;
                return {"result:": "ok"}
            else:
                purchased[buyer] = 1;
                return {"result:": "ok"}
    else:
        message = f"Error: no buyer {buyer}."
        return {"result": message}


@app.get("/buyers/{buyer}/purchased")
async def getPurchased(buyer: str):
    if buyer in purchased:
        value = purchased[buyer]
        return {f"{buyer}:": value}
    else:
        message = f"Error: no buyer {buyer}."
        return {"result": message}
