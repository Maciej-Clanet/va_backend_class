import json

#get profiles
def getProfiles():
    with open("db/profiles.json", "r+") as file:
        return json.load(file)
    
#save profile

#create profile

#get profile by id
def getProfileById(id):
    profiles = getProfiles()

    for profile in profiles["profiles"]:
        if(profile["user_id"] == id):
            return profile

#save profiles
def saveProfiles(newProfiles):
    with open("db/users.json", "w+") as file:
        file.write(json.dumps(newProfiles, indent=4))