docker pull lekhnath12/demo:latest
docker rm -f DEMO
docker run -dit --name DEMO -p 7777:7777 lekhnath12/demo:latest

