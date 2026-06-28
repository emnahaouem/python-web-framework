from wsgiref.simple_server import make_server
from app import App
from response import Response
from template import render, render_with_base
import json
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()
app=App()

def send_email(name, email, message):
    sender=os.getenv("EMAIL")
    password= os.getenv("PASSWORD")
    receiver =os.getenv("EMAIL")

    body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    msg=MIMEText(body)
    msg["Subject"]=f"Portfolioo Contact from {name}"
    msg["From"]= sender
    msg["To"]=receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())

def logger(request):
    print(f"[{request.method}] {request.url}")

app.use(logger)

def home(request):
    return render_with_base("home.html", title="Home")

def about(request):
    return render_with_base("about.html", title="About")

def projects(request):
    return render_with_base("projects.html", title="Projects")

def contact(request):
    if request.method=="POST" :
        data= request.parse_body()
        send_email(data["name"], data["email"], data["message"])
        return render_with_base("contact.html", title="Contact", message=f"Thanks {data['name']}! I'll get back to you soon.")
    return render_with_base("contact.html", title="contact", message="")

app.route("/", home)
app.route("/about",about)
app.route("/projects",projects)
app.route("/contact", contact)
app.route("/contact", contact, method="POST")

print("Server running at http://localhost:8000")
with make_server("",8000,app) as server:
    server.serve_forever()