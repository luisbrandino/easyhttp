class Request:
    def __init__(self, client_connection, request_data,):
        self.client_connection = client_connection
        self.route = request_data['route']
        self.method = request_data['method']
        self.body = request_data['body']
        self.headers = request_data['headers']
        self.params = request_data['params']

    def get_ip(self):
        """Returns the client's origin host.
        
        :return: string
        """

        return self.client_connection.get_ip()

    def get_port(self):
        """Returns the client's origin port.
        
        :return: int
        """

        return self.client_connection.get_port()
    
    def get_method(self):
        """Returns the method of the request.
        
        :return: string
        """

        return self.method
    
    def get_route(self):
        """Returns the requested route.
        
        :return: string
        """

        return self.route