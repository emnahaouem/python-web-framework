import re
class Router:
    def __init__(self):
        self.routes=[]
    
    def add_route(self,method, url, handler):
        pattern=re.sub(r"<(\w+)>", r"(?P<\1>[^/]+)", url)
        print(f"Pattern: {pattern}")
        self.routes.append((method, re.compile("^"+pattern+"$"), handler))

    def match(self,method, url):
        for route_method, pattern, handler in self.routes:
            if route_method != method:
                continue
            m=pattern.match(url)
            if m:
                return handler, m.groupdict()
        return None, {}