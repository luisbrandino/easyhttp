users = [] # The 'database'

def index():
    return users

def create(name, email):
    user = {
        'name': name,
        'email': email
    }

    users.append(user)
    return user

def delete(name):
    for i in range(0, len(users)):
        if users[i]['name'] == name:
            del users[i]
            return True
    
    return False