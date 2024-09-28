from flask import Flask, request, jsonify


app = Flask(__name__)

# Initialize logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return "Hello, Flask is running!"

if __name__ == '__main__':
    app.run(debug=True)
