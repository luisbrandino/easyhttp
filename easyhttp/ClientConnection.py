import _thread

class ClientConnection:
    def __init__(self, conn, addr, socket_server):
        self.conn = conn
        self.ip = addr[0]
        self.port = addr[1]
        self.socket = socket_server
        self.callbacks = []
        
        _thread.start_new_thread(self.handle_connection, ())
        
    def handle_connection(self):
        while True:
            try:
                data = self.conn.recv(1024)
            except OSError:
                self.socket.remove_connection(self)
                
                break
                
            if not data:
                self.socket.remove_connection(self)
            
                break
                
            self.fire_receive_callbacks(data.decode('utf-8'))
     
    def get_conn(self):
        return self.conn
        
    def get_ip(self):
        return self.ip
    
    def get_port(self):
        return self.port

    def get_socket(self):
        return self.socket
    
    def send(self, data):
        self.conn.send(data.encode('utf-8'))

    def close(self):
        self.socket.remove_connection(self)
        
        self.conn.close()
        
    def on_receive(self, callback):
        self.callbacks.append(callback)
    
    def fire_receive_callbacks(self, data):
        for callback in self.callbacks:
            callback(self, data)