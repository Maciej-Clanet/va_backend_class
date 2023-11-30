import json
from db.dbutils import generateUuid

#get users
def getUsers():
    with open("db/users.json", "r+") as file:
        return json.load(file)
        

#getUserById

#addUser

#saveUsers
def saveUsers(newUsers):
    with open("db/users.json", "w+") as file:
        file.write( json.dumps(newUsers, indent=4) )

