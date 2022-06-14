# Final Exam

First of all, you have to install Docker on your PC.

#### Download and Install here:
```
https://www.docker.com/products/docker-desktop/
```
Then download Dockerfile and build image.
#### Building image:
```
docker build -t ANY_TAG .
```

#### Running container:
```
docker run -d -p 8080:8080 ANY_TAG:latest
```

#### Check the program:
```
curl -X POST "http://localhost:8080/buyers?name=BUYER_NAME"
curl -X POST "http://localhost:8080/products?name=PRODUCT_NAME”

curl -X GET "http://localhost:8080/buyers"
curl -X GET "http://localhost:8080/products"

curl -X POST "http://localhost:8080/buyers/BUYER_NAME?prod_name=PRODUCT_NAME”

curl -X GET "http://localhost:8000/buyers/BUYER_NAME/purchased”
```

