import json
from datetime import datetime
from db.userUtils import getUserById

def getArtworks():
    with open("db/artworks.json", "r+") as file:
        return json.load(file)
    
def saveArtworks(new_artworks):
    with open("db/artworks.json", "w+") as file:
        file.write(json.dumps(new_artworks, indent=4))

def addArtwork(user_id, category, title, description, image_url, tags):
    artworks = getArtworks()
    thumbPath = f"http://localhost:8000/static/users/{user_id}/thumbnails/{title}.png"
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