from requests import status_codes
import json
import codecs

class Response:
    def __init__(self, client_connection):
        self.client_connection = client_connection
        self.status_text = 'OK'
        self.status_code = 200

        self.headers = {
            'Content-Type': 'text/html; encoding=utf8',
            'Connection': 'close',
        }

    def set_status(self, status_code):
        """Defines the status code of the response, if it is valid.
        
        :param status_code: status code to be defined

        :return: Response
        """

        if not status_code in status_codes._codes:
            return self
        
        self.status_text = status_codes._codes[status_code][0].upper()
        self.status_code = status_code
        return self

    def send_file(self, file_path):
        """Tries to send an static file as the response. If the path doesn't exist, it will send an HTTP 404.
        
        :param file_path: path of the file
        """

        try:
            file = codecs.open(file_path, 'r', 'utf-8')
            self.send(file.read())
        except (FileNotFoundError, OSError):
            self.send_404()
    
    def send_404(self):
        """Sends an HTTP 404."""

        self.set_status(404).send('<h1>Not Found</h1>')
    
    def json(self, data):
        """Sends the response as a JSON.
        
        :param data: dictionary to be sent as JSON
        """

        data = json.dumps(data)

        self.headers['Content-Type'] = 'application/json; encoding=utf8'

        self.send(data)

    def send(self, content):
        """Sends the response with the specified content.
        
        :param content: data to be sent as response
        """

        conn = self.client_connection

        conn.send(self.__prepare_response(content))

        conn.close()

    def __prepare_response(self, content):
        self.headers['Content-Length'] = len(content)

        response = f'HTTP/1.1 {self.status_code} {self.status_text}\r\n'

        return f'{response}{self.__parse_headers()}\r\n{content}'

    def __parse_headers(self):
        return ''.join('%s: %s\r\n' % (k, v) for k, v in self.headers.items())