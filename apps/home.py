
import flask
import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from yandex_geocoder import Client
from flask import current_app



router_home = flask.Blueprint('router_home', __name__)


@router_home.route('/')
def home():
    '''
    return message as json with a little documentation documentation.
    '''
    res = {
        "Resume": "Api to get find distance from the Moscow Ring Road to the specified addressy.",
        "/getDistanceFromMoscou/<address>}/'": "Send a GET request over HTTP with destiny param <address>"
    }
    return flask.jsonify(res)