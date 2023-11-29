import json
from datetime import datetime

def getProducts():
    with open("db/products.json", "r+") as file:
        return json.load(file)

def saveProducts(new_products):
    with open("db/products.json", "w+") as file:
        file.write(json.dumps(new_products, indent=4))

def addProduct(user_id, category, title, description, price, image_url):
    products = getProducts()
    products["products"].append({
        "user_id": user_id,
        "category" :category,
        "title" : title,
        "description" : description,
        "price" : price,
        "image_url" : image_url,
        "created_at" : datetime.now().isoformat()
    })
    saveProducts(products)

def getProductsByUser(user_id):
    products = getProducts()
    user_products = []
    for product in products["products"]:
        if product["user_id"] == user_id:
            user_products.append(product)
    return user_products