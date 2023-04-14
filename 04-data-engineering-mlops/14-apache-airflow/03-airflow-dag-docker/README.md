#### Build the Docker file
1. Build the image using docker-compose up -d --build
2. Run the webserver - docker-compose up
3. go to http://localhost:8080, Turn on DAG and check the status of the task.
4. docker-compose down # turns down the container
#### Writing the DAG
Steps to remember
1. Importing modules.
2. Default arguments.
3. Instantiate a DAG
4. Tasks
5. Setup dependencies.
