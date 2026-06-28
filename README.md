# Python Web Framework
A lightweight web framework built from scratch in Python : no Flask, no Django, just Pure python.

## Features:
URL routing engine with dynamic routes ('/users/<id>')
Middleware pipeline
Template engine with base layout support
Static file serving
POST body parsing
JSON support
WSGI compatible

## Project Structure
app.py # Core framework class
router.py # URL routing engine
middleware.py # Middleware pipeline
request.py # HTTP Response object
template.py # Template engine
server.py # Portfolio app built on the framework
templates/ # HTML templates
static/ # CSS files

## Demo
This repo includes a portfolio website built on top of the framework.

## How to run
''' bash
python server.py
'''

then visit 'http:localhost:8000'

## built by
Emna Haouem Network & Systems Engineering Student