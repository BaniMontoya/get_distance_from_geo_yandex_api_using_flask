from logging.handlers import RotatingFileHandler
import logging
import flask
import geo as geo
import home as home

# create application
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# import blueprints
app.register_blueprint(geo.router_geo)
app.register_blueprint(home.router_home)

#logging setup
file_handler = RotatingFileHandler(
    'logs/all_logs.log', maxBytes=1024 * 1024 * 100, backupCount=20)
file_handler.setLevel(logging.DEBUG)
app.logger.setLevel(logging.INFO)
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)

# run application
if __name__ == "__main__":
    app.run(host='0.0.0.0')