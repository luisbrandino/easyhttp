import UsersController

def route(app):
    app.get('/users', UsersController.index)
    app.post('/users', UsersController.create)
    app.delete('/users', UsersController.delete)