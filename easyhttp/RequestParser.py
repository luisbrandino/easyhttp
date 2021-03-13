from urllib.parse import urlsplit, parse_qs, parse_qsl
from io import StringIO
import json
import email

class RequestParser:
    def parse(self, data):
        raw_request, raw_headers = data.split('\r\n', 1)
        raw_body = raw_headers.split('\r\n')[-1]

        headers = self.parse_headers(raw_headers)
        method = self.parse_method(raw_request)
        url = self.parse_url(raw_request)
        route = self.parse_route(raw_request)
        body = self.parse_body(headers, raw_body)
        params = self.parse_query_params(url)

        return {
            'method': method,
            'route': route,
            'headers': headers,
            'body': body,
            'params': params
        }
    
    def parse_headers(self, raw_headers):
        message = email.message_from_file(StringIO(raw_headers))

        return dict(message.items())

    def parse_query_params(self, url):
        return dict(parse_qsl(urlsplit(url).query))

    def parse_method(self, raw_request):
        return raw_request.split(' ')[0].strip().lower()

    def parse_url(self, raw_request):
        return raw_request.split(' ')[1].strip()

    def parse_route(self, raw_request):
        return raw_request.split(' ')[1].split('?')[0].strip()

    def parse_urlencoded_body(self, raw_body):
        return dict(parse_qsl(raw_body))

    def parse_json_body(self, raw_body):
        return json.loads(raw_body)

    def parse_body(self, headers, raw_body):
        if not 'Content-Type' in headers: return None

        content_type = headers['Content-Type']

        content_type = content_type.replace('application/', '').split('-')[-1]

        attribute = f'parse_{content_type}_body'
        
        if not hasattr(self, attribute): return None

        return getattr(self, attribute)(raw_body)
