from flask import Flask
from routes import api
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(api)

CORS(app)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
