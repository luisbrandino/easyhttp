from .ClientConnection import ClientConnection
import socket

class SocketServer:
    def __init__(self, host='0.0.0.0', port=0):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen()
        self.connections = []

    def get_host(self):
        return self.host
    
    def get_port(self):
        return self.port
    
    def remove_connection(self, client_connection_to_remove):
        index = 0
        found = False
        
        for client_connection in self.connections:
            if client_connection == client_connection_to_remove:
                found = True
                break
                
            index += 1
            
        if found: del self.connections[index]
    
    def accept(self):
        conn, addr = self.socket.accept()
        
        client_connection = ClientConnection(conn, addr, self)
        
        self.connections.append(client_connection)
                
        return client_connection