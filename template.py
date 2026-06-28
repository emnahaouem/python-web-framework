from response import Response

def render (filename, **kwargs):
    with open(f"templates/{filename}","r") as f:
        content=f.read()
    for key, value in kwargs.items():
        content=content.replace(f"{{{{ {key} }}}}",value)
    return Response(body=content)

def render_with_base(filename, **kwargs):
    with open("templates/base.html", "r") as f:
        base=f.read()
    with open(f"templates/{filename}", "r") as f:
        content=f.read()
    base=base.replace("{{ content }}", content)
    for key, value in kwargs.items():
        base=base.replace(f"{{{{ {key} }}}}", value)
    return Response(body=base)