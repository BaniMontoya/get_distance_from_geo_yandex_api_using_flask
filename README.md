# get_distance_from_geo_yandex_api_using_flask

original requirement from Voctiv.

Problem statement: 
 
Develop a Flask Blueprint to find the distance from the Moscow Ring Road to the specified 
address. The address is passed to the application in an HTTP request, if the specified address is 
located inside the MKAD, the distance does not need to be calculated. Add the result to the .log 
file 
To calculate the distance between points, we suggest using the Yandex Geocoder API 
https://yandex.ru/dev/maps/geocoder/doc/desc/concepts/about.html 
The developer key can be obtained for free upon registration. 
 
You need to implement: 
1. Directly Blueprint 
2. A set of Unit tests and corner cases checks (for example, invalid input data) 
3. Documenting the code and application 
 
Requirements: 
1. The address is transmitted via an HTTP request 
2. The functions and algorithms used are provided with informative comments 
3. The tests are arranged in a separate file 
4. Documentation in the form of readme.md the file contains instructions for using the 
application 
5. PEP8 code compliance and use of type annotations 
 
Requirements for tools: 
1. Python version no older than 3.8 
2. Source code must be published on Github/Gitlab/Bitbucket 
3. It will be a plus to create a Docker container with the application 


***********************************
INSTALATION:

Get this libraries:

+ Flask
+ Yandex Geo API
+ Shapely
+ Numpy
+ Pytest
+ Yandex-geocoder

Steps:

1. 