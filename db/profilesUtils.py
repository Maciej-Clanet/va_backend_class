import json

#get profiles
def getProfiles():
    with open("db/profiles.json", "r+") as file:
        return json.load(file)

#save profiles
def saveProfiles(newProfiles):
    with open("db/profiles.json", "w+") as file:
        file.write(json.dumps(newProfiles, indent=4))

#get profile by id
def getProfileById(id):
    profiles = getProfiles()

    for profile in profiles["profiles"]:
        if id == profile["user_id"]:
            return profile


#save profile

#create profile

#get profile by id

#save profiles