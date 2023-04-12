#### About
Airflow is built to integrate with all databases, system and cloud environments
Challenges that airflow has with huge subpackages under the belt - 
* Managing and maintaining all of the dependencies changes are very difficult.
* Takes a lot of time to setup and config airflow env
* Hard to share development and production environments for all developers.

> Solution to the quoted challenges
- Dockers.

> Pre-requisites
- Docker
- docker-compose

> command to execute.
1. Build the image using docker-compose up -d --build
1. Run the webserver - docker-compose up
2. go to http://localhost:8080
3. docker-compose down # turns down the container

> Error resolution
1. ERROR: Get "https://registry-1.docker.io/v2/": net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)
- Resolution 
1. Go to /etc/resolv.conf
2. add the following nameservers
```
nameserver 8.8.8.8
nameserver 8.8.4.4
nameserver 127.0.0.53
```