from urllib.parse import unquote_plus

class Request:
    def __init__(self, method, url, body):
        self.method=method
        self.url=url
        self.body=body
    def parse_body(self):
        parts=self.body.split("&")
        result={}
        for i in parts:
            key, value = i.split("=")
            result[key]=unquote_plus(value)
        return result