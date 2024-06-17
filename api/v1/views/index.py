#!/usr/bin/python3

"""
Create Flask app
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/status', methods=['GET', ])
def api_status():
    """
    Returns the status of the API
    """
    response = {'status': 'OK'}
    return jsonify(response)

@app_views.route('/stats')
def get_stats():
    """
    """
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }

    return jsonify(stats)