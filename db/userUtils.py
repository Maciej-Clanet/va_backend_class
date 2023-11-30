import json
from db.dbutils import generateUuid

#get users
def getUsers():
    with open("db/users.json", "r+") as file:
        return json.load(file)
        

#getUserById

#addUser

#saveUsers

