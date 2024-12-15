from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello_world():
    # Return the string 'Hello, World!' to the client
    return 'Hello, World'

# Check if the script is being run directly (not imported)
if __name__ == '__main__':
    # Run the Flask application
    app.run()
