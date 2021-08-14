
import logging

from shapely.geometry import Point, Polygon
from shapely.ops import nearest_points

import flask
import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from yandex_geocoder import Client

LONS = [37.842762, 37.842789, 37.842627, 37.841828, 37.841217, 37.840175, 37.83916, 37.837121, 37.83262, 37.829512, 37.831353, 37.834605, 37.837597, 37.839348, 37.833842, 37.824787, 37.814564, 37.802473, 37.794235, 37.781928, 37.771139, 37.758725, 37.747945, 37.734785, 37.723062, 37.709425, 37.696256, 37.683167, 37.668911, 37.647765, 37.633419, 37.616719, 37.60107, 37.586536, 37.571938, 37.555732, 37.545132, 37.526366, 37.516108, 37.502274, 37.49391, 37.484846, 37.474668, 37.469925, 37.456864, 37.448195, 37.441125, 37.434424, 37.42598, 37.418712, 37.414868, 37.407528, 37.397952, 37.388969,
        37.383283, 37.378369, 37.374991, 37.370248, 37.369188, 37.369053, 37.369619, 37.369853, 37.372943, 37.379824, 37.386876, 37.390397, 37.393236, 37.395275, 37.394709, 37.393056, 37.397314, 37.405588, 37.416601, 37.429429, 37.443596, 37.459065, 37.473096, 37.48861, 37.5016, 37.513206, 37.527597, 37.543443, 37.559577, 37.575531, 37.590344, 37.604637, 37.619603, 37.635961, 37.647648, 37.667878, 37.681721, 37.698807, 37.712363, 37.723636, 37.735791, 37.741261, 37.764519, 37.765992, 37.788216, 37.788522, 37.800586, 37.822819, 37.829754, 37.837148, 37.838926, 37.840004, 37.840965, 37.841576]
LATS = [55.774558, 55.76522, 55.755723, 55.747399, 55.739103, 55.730482, 55.721939, 55.712203, 55.703048, 55.694287, 55.68529, 55.675945, 55.667752, 55.658667, 55.650053, 55.643713, 55.637347, 55.62913, 55.623758, 55.617713, 55.611755, 55.604956, 55.599677, 55.594143, 55.589234, 55.583983, 55.578834, 55.574019, 55.571999, 55.573093, 55.573928, 55.574732, 55.575816, 55.5778, 55.581271, 55.585143, 55.587509, 55.5922, 55.594728, 55.60249, 55.609685, 55.617424, 55.625801, 55.630207, 55.641041, 55.648794, 55.654675, 55.660424, 55.670701, 55.67994, 55.686873, 55.695697, 55.702805, 55.709657,
        55.718273, 55.728581, 55.735201, 55.744789, 55.75435, 55.762936, 55.771444, 55.779722, 55.789542, 55.79723, 55.805796, 55.814629, 55.823606, 55.83251, 55.840376, 55.850141, 55.858801, 55.867051, 55.872703, 55.877041, 55.881091, 55.882828, 55.884625, 55.888897, 55.894232, 55.899578, 55.90526, 55.907687, 55.909388, 55.910907, 55.909257, 55.905472, 55.901637, 55.898533, 55.896973, 55.895449, 55.894868, 55.893884, 55.889094, 55.883555, 55.877501, 55.874698, 55.862464, 55.861979, 55.850257, 55.850383, 55.844167, 55.832707, 55.828789, 55.821072, 55.811599, 55.802781, 55.793991, 55.785017]

geo = flask.Blueprint('geo', __name__)

logging.basicConfig(level=logging.DEBUG, filename="all_logs.log", filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")

def calculateDistanceFromMoscou(y, x):
    '''
    calculateDistanceFromMoscou
    '''
    distance = 0
    point = Point(y, x)
    polygon = Polygon(np.column_stack((LONS, LATS)))
    p1, p2 = nearest_points(polygon, point)
    if  polygon.contains(point):
        return str(0), str(0)
    else:
        distanceInDegrees = Point(p1).distance(Point(p2))
        logging.info(" Google Maps link, " +
                     f"https://www.google.com.ec/maps/dir/{p1.y},{p1.x}/{p2.y},{p2.x}/@{p1.y},{p1.x},11z/")
        logging.info(
            "··································································")
        distanceInMeters = distanceInDegrees*111.139*1000
        return str(distanceInMeters), str(distanceInDegrees)


@geo.route('/getDistanceFromMoscou/<destiny>/', methods=['GET'])
def getDistanceFromMoscou(destiny):
    '''
    Endpoint to get find distance from the Moscow Ring Road to the specified addressy .
    '''
    client = Client("43c7e76d-3153-490e-b25f-72f105c21c74")
    try:
        y, x = client.coordinates(destiny.replace("+", " "))
        distanceInMeters, distanceInDegrees = calculateDistanceFromMoscou(y, x)
        if distanceInDegrees == 0 and distanceInMeters == 0:
            return flask.jsonify({"Message":"Is Inside Moscow Ring Road"})

        else:
            return flask.jsonify({"distanceInMeters": distanceInMeters, "distanceInDegrees": distanceInDegrees})
    except:
        return flask.jsonify({"Message": "Is an Invalid address, you can fix and try again."})
