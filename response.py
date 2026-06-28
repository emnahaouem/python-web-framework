import json

class Response:
    def __init__(self, status=200, body="", content_type="text/html"):
        self.status=status
        self.body=body
        self.content_type=content_type

    def json(self, data):
        body=json.dumps(data)
        return Response(body=body, content_type="application/json")