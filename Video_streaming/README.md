## To pull images for frontend and backend project type the next commands

### backend:

docker pull maherreramu/node_streaming_backend:v1.0

### frontend:

docker pull maherreramu/node_streaming_frontend:v1.0


## To run the containers from the images type the next commands

### backend:

docker run -d --name streaming_backend -v streaming_backend:/usr/src/app -p 5000:5000 maherreramu/node_streaming_backend:v1.0

### frontend:

docker run -d --name streaming_frontend -p 3000:3000 maherreramu/node_streaming_frontend:v1.0


To add the video library read the txt at backend/assets folder