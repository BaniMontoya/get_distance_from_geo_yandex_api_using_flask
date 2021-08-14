# get_distance_from_geo_yandex_api_using_flask

***********************************
INSTALATION and USE:

1. get code
1.1 clone
>> git clone https://github.com/BaniMontoya/get_distance_from_geo_yandex_api_using_flask.git

2. access directory
>> cd get_distance_from_geo_yandex_api_using_flask

3. update key
>> get an key on https://developer.tech.yandex.ru/services/ or use the provided key and 
update KEY value on file apps/geo.py


4. execute installation
>> sh install.sh

5. Using with curl

>> curl http://127.0.0.1:5000/getDistanceFromMoscou/E22,%20Moskva,%20Rusia,%20121500/

{
  "distanceInDegrees": "0", 
  "distanceInMeters": "0"
}

>> curl http://127.0.0.1:5000/getDistanceFromMoscou/1/

{
  "Message": "Invalid address, you can fix and try again."
}
