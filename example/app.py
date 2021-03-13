import UsersRoutes
import easyhttp

app = easyhttp.App()

UsersRoutes.route(app)

def server_started():
    print('Server up and running!')

app.listen(3000, server_started)