import json
import uuid
from datetime import datetime

def generateUuid():
    return uuid.uuid4().hex

def getUsers():
    with open("db/users.json", "r+") as file:
        return json.load(file)

def getUserById(id):
    with open("db/users.json", "r+") as file:
        users = json.load(file);
        for user in users["users"]:
            if user["id"] == id:
                return user
        return None
    
def addUser(username, email, password):
    users = getUsers()
    users["users"].append({
        "id" : generateUuid(),
        "username": username,
        "email": email,
        "password" : password
    })
    saveUsers(users)

def saveUsers(new_users):
    with open("db/users.json", "w+") as file:
        file.write(json.dumps(new_users, indent=4))

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

def getArtworks():
    with open("db/artworks.json", "r+") as file:
        return json.load(file)
    
def saveArtworks(new_artworks):
    with open("db/artworks.json", "w+") as file:
        file.write(json.dumps(new_artworks, indent=4))

def addArtwork(user_id, category, title, description, image_url, tags):
    artworks = getArtworks()
    thumbPath = f"http://localhost:8000/static/user_art/{user_id}/thumbnails/{title}.png"
    thumbPath = thumbPath.replace(" ", "%20")

    artworks["artworks"].append({
        "user_id" : user_id,
        "username" : getUserById(user_id)["username"],
        "category" : category,
        "title" : title,
        "description" : description,
        "image_url" : image_url,
        "thumbnail_path": thumbPath,
        "tags" : tags,
        "created_at" : datetime.now().isoformat()
    })
    saveArtworks(artworks)

def getArtworksByUser(user_id):
    artworks = getArtworks()
    user_artworks = []
    for art in artworks["artworks"]:
        if art["user_id"] == user_id:
            user_artworks.append(art)
    return user_artworks


def getLatestArtworks(amount):
    artworks = getArtworks()

    sorted_artworks = sorted(artworks["artworks"], key=lambda art: art["created_at"], reverse=True )

    return sorted_artworks[:min(amount, len(sorted_artworks))]