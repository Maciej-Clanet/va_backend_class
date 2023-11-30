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
        "bio" : "",
        "art_categories" : ["all"],
        "product_categories" : ["all"]
    }

    profiles = getProfiles()
    profiles["profiles"].append(profileInfo)
    saveProfiles(profiles)

def getProfileById(id):
    profiles = getProfiles()["profiles"]
    for profile in profiles:
        if(profile["user_id"] == id):
            return profile
        
def saveProfileChange(id, newData):
    profiles = getProfiles()

    for profile in profiles["profiles"]:
        if(profile["user_id"] == id):
            profile.update(newData)
            print(profile)
            break
    print(profiles)
    saveProfiles(profiles)