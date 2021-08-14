import flask
from .geo_routes import geo

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.register_blueprint(geo)


@app.route('/')
def home():
    '''
    return message as json with a little documentation documentation.
    '''
    return flask.jsonify({"Resume": "Api to get find distance from the Moscow Ring Road to the specified addressy.", "distance/MKAD/<address>/": "Send a GET request over HTTP with destiny param <address>, example: distance/MKAD/address/"})
