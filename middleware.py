class Middleware:
    def __init__(self):
        self.middleware=[]
    def add(self,func):
        self.middleware.append(func)
    def run(self, request):
        for i in self.middleware:
            i(request)