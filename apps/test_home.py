# test_hello.py
import logging
from unittest import TestCase
import json
from run import app

LOGGER = logging.getLogger(__name__)


class AppTest(TestCase):

    def test_home(self):
        """
        [testing home path]
        """
        response = app.test_client().get('/')
        assert response.status_code == 200

    def test_distance(self):
        """
        [All tests of getDistanceFromMoscou ]
        """
        # testing worng path
        response = app.test_client().get('/getDistanceFromMoscou')
        assert response.status_code == 404
        # testing  correct path and correct addres, inside
        address = "Tikhoretskiy Bul'var, 1, Moscow, Rusia, 109559"
        response = app.test_client().get(
            f'/getDistanceFromMoscou/{address.replace(" ","+")}/')
        LOGGER.info("response: "+str(json.loads(response.data)))
        assert response.status_code == 200
        assert json.loads(response.data)['distanceInMeters'] == "0"
        # correct path and outside
        address = "Ulitsa Narodnogo Opolcheniya, 15, Krasnogorsk, Moscow Oblast, Rusia, 143403"
        response = app.test_client().get(
            f'/getDistanceFromMoscou/{address.replace(" ","+")}/')
        LOGGER.info("response: "+str(json.loads(response.data)))
        assert response.status_code == 200
        assert json.loads(response.data) == {
            'distanceInDegrees': '0.07486909753029411', 'distanceInMeters': '8320.876630419356'}
        # correct path and worng address
        address = "NOEXIST"
        response = app.test_client().get(
            f'/getDistanceFromMoscou/{address.replace(" ","+")}/')
        LOGGER.info("response: "+str(json.loads(response.data)))
        assert response.status_code == 400
        assert json.loads(response.data) == {
            'Message': 'Invalid address, you can fix and try again.'}
