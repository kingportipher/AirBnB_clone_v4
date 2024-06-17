#!/usr/bin/python3

"""
Create Flask app
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_db(exception):
    """
    close storage
    """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """Handler for 404 errors that returns a JSON-formatted response"""
    response = jsonify({"error": "Not found"})
    response.status_code = 404
    return response


if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=HOST, port=PORT, threaded=True)
