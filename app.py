from router import Router
from middleware import Middleware
from request import Request
from response import Response

class App:
    def __init__(self):
        self.router=Router()
        self.middleware=Middleware()
    
    def use(self, func):
        self.middleware.add(func)
    def route(self, url, handler, method="GET"):
        self.router.add_route(method,url,handler)
    def run(self,url, method, body=""):
        request=Request(method, url, body)
        self.middleware.run(request)
        handler, url_params=self.router.match(method,url)
        if handler is not None:
            return handler(request, **url_params)
        else:
            return Response(status=404,body="Not Found")
        
    def __call__(self, environ, start_response):
        try:
            url=environ["PATH_INFO"]
            method=environ["REQUEST_METHOD"]
            content_length=int(environ.get("CONTENT_LENGTH",0) or 0)
            body=environ["wsgi.input"].read(content_length).decode("utf-8")
            if url.startswith("/static/"):
                filepath=url[1:]
                with open(filepath, "r") as f:
                    content=f.read()
                response=Response(body=content, content_type="text/css")
            else:
                response = self.run(url, method, body)
            status_message= {200:"OK", 404:"Not Found", 500:"Internal Server Error"}
            status=f"{response.status} {status_message.get(response.status, 'OK')}"
            headers =[("Content-Type", response.content_type)]
            start_response(status, headers)
            return [response.body.encode("utf-8")]
        except Exception as e:
            print(f"ERROR: {e}")
            raise