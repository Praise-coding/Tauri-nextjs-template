from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

@app.route('/')
def home():
    data = {"word"  :'Hello from Flask!' }
    return jsonify(data) 

if __name__ == '__main__':
    app.run(debug=True)
