import UsersModel

def index(req, res):
    users = UsersModel.index()

    return res.set_status(201).json(users)

def create(req, res):
    if not 'name' in req.body or not 'email' in req.body:
        return res.set_status(400).json({ 'message': 'Missing fields' })

    user = UsersModel.create(req.body['name'], req.body['email'])
    return res.set_status(201).json(user)

def delete(req, res):
    if not 'name' in req.body:
        return res.set_status(400).json({ 'message': 'Missing fields' })

    if UsersModel.delete(req.body['name']):
        return res.set_status(201).json({ 'message': 'User successfully deleted' })

    res.set_status(500).json({ 'message': 'Something went wrong' })
