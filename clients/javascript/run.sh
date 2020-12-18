#docker rm -f coba-webix-server;
#docker run -d --name coba-webix-server -p 34000:9999 contoh-webserver-webix

docker run -dti --rm -p 9999:9999 -e BASEURL="http://localhost:35001" --name JSCLIENT my-phonebook-service-clients-js:latest
