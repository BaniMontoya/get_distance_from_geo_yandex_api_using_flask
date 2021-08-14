# stop process with the app name
docker ps -q --filter ancestor="get_distance_from_moscou_app" | xargs -r docker stop
# force delete old images with app name
docker rmi $(docker images 'get_distance_from_moscou_app' -a -q) --force
# build container
docker build -t get_distance_from_moscou_app .
# run container
docker run  -dp 5000:5000 get_distance_from_moscou_app
# run tests
docker exec   $(docker ps | grep 'get_distance_from_moscou_app' | awk '{ print $1 }') py.test
