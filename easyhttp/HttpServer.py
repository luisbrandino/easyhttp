from .SocketServer import SocketServer
from .RequestParser import RequestParser
from .Request import Request
from .Response import Response

class App:
    def __init__(self):
        self.routes = {
            'get': {},
            'post': {},
            'put': {},
            'delete': {}
        }

        self.public_folder = None

    def get(self, route, callback):
        """Calls the callback whenever an HTTP GET request is made to the specified route.
        
        :param route: route for which the callback is called
        :param callback: callback function
        """

        self.routes['get'][route] = callback

    def post(self, route, callback):
        """Calls the callback whenever an HTTP POST request is made to the specified route.
        
        :param route: route for which the callback is called
        :param callback: callback function
        """

        self.routes['post'][route] = callback

    def put(self, route, callback):
        """Calls the callback whenever an HTTP PUT request is made to the specified route.
        
        :param route: route for which the callback is called
        :param callback: callback function
        """

        self.routes['put'][route] = callback

    def delete(self, route, callback):
        """Calls the callback whenever an HTTP DELETE request is made to the specified route.
        
        :param route: route for which the callback is called
        :param callback: callback function
        """

        self.routes['delete'][route] = callback
    
    def public(self, public_folder_path):
        """Defines a public directory to serve static content such as JS and CSS.
        
        :param public_folder_path: path of the public folder
        """

        self.public_folder = public_folder_path

    def listen(self, port=0, callback=None):
        """
        Starts web server and listens for connections on the specified port. 
        If port is not specified, it will find an unused local port. 
        Once the web server is started, callback will be called, if defined. 

        :param port: port to be opened (optional)
        :param callback: callback function (optional)
        """

        self.port = port
        self.socket = SocketServer('0.0.0.0', self.port)

        if callback: callback()

        while True:
            client_connection = self.socket.accept()
            
            client_connection.on_receive(self.on_request)

    def on_request(self, client_connection, data):
        request_data = RequestParser().parse(data)

        request, response = self.__create_request_and_response(client_connection, request_data)

        route = self.__get_route(request.get_method(), request.get_route())

        if not route:
            if not self.public_folder or request.get_method() != 'get':
                return response.send_404()

            return response.send_file(f'{self.public_folder}{request.get_route()}')

        route(request, response)

    def __get_route(self, method, route):
        if route in self.routes[method]:
            return self.routes[method][route]
        
        return None

    def __create_request_and_response(self, client_connection, request_data):
        return Request(client_connection, request_data), Response(client_connection)