# test_hello.py
from apps.home import app
from unittest import TestCase
import logging


class AppTest(TestCase):
    def setUp(self) -> None:
        logging.basicConfig(level=logging.DEBUG, filename="tests_logs.log", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
        return super().setUp()
    
    def test_home(self):
        response = app.test_client().get('/')
        assert response.status_code == 200

    def test_distance(self):
        # testing worng url
        response = app.test_client().get('/getDistanceFromMoscou')
        assert response.status_code == 404
        # testing  correct url and correct addres, inside
        address = "Tikhoretskiy Bul'var, 1, Moscow, Rusia, 109559"
        response = app.test_client().get(f'/getDistanceFromMoscou/{address.replace(" ","+")}/')
        logging.info(response.data)

        assert response.status_code == 200
        assert response.data[0] == "0"
        # correct url and outside
        address = "Ulitsa Narodnogo Opolcheniya, 15, Krasnogorsk, Moscow Oblast, Rusia, 143403"
        response = app.test_client().get(f'/getDistanceFromMoscou/{address.replace(" ","+")}/')
        assert response.status_code == 200

#assert coordinates == (Decimal("37.587093"), Decimal("55.733969"))
 
'''

polygon = Polygon(np.column_stack((lon, lat)))

x = -0.1081339
y = 78.4699519
point = Point(y, x)
print(polygon.contains(point))
print(point.within(polygon))

# true
x2 = 55.825279
y2 = 37.5974423
point = Point(y2, x2)
print(polygon.contains(point))
print(point.within(polygon))

# true
x3 = 55.6743768
y3 = 37.7414324
point = Point(y3, x3)
print(polygon.contains(point))
print(point.within(polygon))

# false
x4 = 55.9227296
y4 = 37.6882454, 13
point = Point(y4, x4)
print(polygon.contains(point))
print(point.within(polygon))


'''
