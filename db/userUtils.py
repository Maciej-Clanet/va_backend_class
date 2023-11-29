import json
from db.dbutils import generateUuid

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
