from flask import Flask, render_template

app = Flask(__name__)

# Define routes and views for the application
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def test():
    return render_template('test.html')

# Create a WSGI callable object that wraps the app instance
def run_app():
    return app

if __name__ == '__main__':
    app.run(debug=True)
