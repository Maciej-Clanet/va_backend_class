import json

def getProfiles():
    with open("db/profiles.json", "r+") as file:
        return json.load(file)
    
def saveProfiles(new_profiles):
    with open("db/profiles.json", "w+") as file:
        file.write(json.dumps(new_profiles, indent=4))

def createProfile(id):

    profileInfo = {
        "user_id": id,
        "bio" : None,
        "categories" : []
    }