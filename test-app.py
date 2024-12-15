from flask import Flask

app = Flask(__name__)

# Define routes and views for the application
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Create a WSGI callable object that wraps the app instance
def run_app():
    return app

# Alternatively, you can use the `make_wsgi_app` function from Flask
from flask import make_wsgi_app
wsgi_app = make_wsgi_app(app)
