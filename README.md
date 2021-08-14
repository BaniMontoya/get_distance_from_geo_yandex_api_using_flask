# get_distance_from_geo_yandex_api_using_flask

***********************************
INSTALATION:

Python 3.8

Get this token key:
+ Yandex Geo API

Get this Python libraries installed:

+ Flask
+ Shapely
+ Numpy
+ Pytest
+ Yandex-geocoder

Steps:

1. get code
1.1 clone
>> git clone https://github.com/BaniMontoya/get_distance_from_geo_yandex_api_using_flask.git
1.2 update key
get an key on https://developer.tech.yandex.ru/services/ or use the provided key and 
update KEY value on file apps/geo.py

2. access directory
>> cd get_distance_from_geo_yandex_api_using_flask

3. execute installation
>> sh install.sh

4. Using with curl
4.1. example 1
>> curl http://127.0.0.1:5000/getDistanceFromMoscou/E22,%20Moskva,%20Rusia,%20121500/
return {
  "distanceInDegrees": "0", 
  "distanceInMeters": "0"
}
4.2. example 2
>> curl http://127.0.0.1:5000/getDistanceFromMoscou/1/
{
  "Message": "Invalid address, you can fix and try again."
}
