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
    new_id = generateUuid()
    users["users"].append({
        "id" : new_id,
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
    artworks["artworks"].append({
        "user_id" : user_id,
        "category" : category,
        "title" : title,
        "description" : description,
        "image_url" : image_url,
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

    #you can think of lambdas as an anonymous function in react
    #if we pretend this was react, sorted would look a bit like
    #sorted( theListToSort, (art) => {return art["created_at"]}, reverse=true )
    #there are differences, anon functions can do more, but this is the basic gist fo it
    sorted_artworks = sorted(artworks["artworks"], key=lambda art: art["created_at"], reverse=True )

    #only return as much artworks as are available (up to the requested amount), prevents out of range errors
    #min just checks which value "amount" or "len(sorted_artworks)" is smaller and returns it
    return sorted_artworks[:min(amount, len(sorted_artworks))]